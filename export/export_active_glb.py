import os
import re
import subprocess
import bpy

from bpy_extras.io_utils import ExportHelper

from . export_glb import export_glb
from .. B2REACT_Globals import get_project_root, get_project_name


class B2REACT_OT_Export_Active_GLB(bpy.types.Operator, ExportHelper):
    """Export Active Collectios as GLB file"""

    bl_idname = "blender2react.export_active_glb"
    bl_label = "Export Active Collection as GLB"

    bl_description = "Export All Collections as separated GLB files"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    filename_ext = ".glb"

    filter_glob: bpy.props.StringProperty(
        default="*.glb",
        options={'HIDDEN'},
    )

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        print("_____________________________________________________________")
        print("Exporting Active Collections as GLB file...")

        # Abort if no export path is set
        if not context.scene.Blender2React.R3F_Export_Path:
            print("WARNING: No Export Path set.")
            self.report({'ERROR'}, "No Export Path set.")
            return {'CANCELLED'}

        # Convert relative path to absolute path if //
        if context.scene.Blender2React.R3F_Export_Path.startswith("//"):
            context.scene.Blender2React.R3F_Export_Path = bpy.path.abspath(context.scene.Blender2React.R3F_Export_Path)

        # Get the actual frame number and Move the timeline to the last frame
        # to avoid animation issues on scale
        current_frame = context.scene.frame_current
        context.scene.frame_set(context.scene.frame_end)
        context.view_layer.update()

        # Create a dictionary to store the collection names and exclude attribute status
        # current_collection_status = {}
        # for LayerCollection in context.scene.view_layers[0].layer_collection.children:
        #     current_collection_status[LayerCollection.name] = LayerCollection.exclude
        # print("current_collection_status:", current_collection_status)

        active_collection = context.view_layer.active_layer_collection

        # print("active_collection:", active_collection)
        # print("collection:", active_collection.name, "exclude:", active_collection.exclude)
        # print("Exporting collection:", active_collection.name)

        # Iterate over all the LayerCollections and exclude all but the active one
        # for LayerCollection in context.scene.view_layers[0].layer_collection.children:
        #     # If the LayerCollection starts with a _ ignore it
        #     if LayerCollection.name != active_collection.name:
        #         LayerCollection.exclude = True
        #         print("collection:", LayerCollection.name, "exclude:", LayerCollection.exclude)

        print()
        print("-------------------------------------------------------------")
        print("-------------- EXPORT ACTIVE COLLECTION AS GLB --------------")
        print("-------------------------------------------------------------")
        print()

        # Set the filepath from the export path and the collection name
        filepath = os.path.join(context.scene.Blender2React.R3F_Export_Path, active_collection.name)
        print("filepath:", filepath)
        print()

        # Export the GLB file
        export_glb(filepath, active=True)

        # Launch gltfjsx command
        glft_jsx_cmd = f"cd {context.scene.Blender2React.R3F_Export_Path}\
                && npx gltfjsx {filepath}.glb\
                --output {filepath}.glb\
                --keepnames\
                --keepgroups\
                --instance\
                --printwidth 150\
                --root {context.scene.Blender2React.R3F_Export_Path}\
                --transform\
                --shadows\
                --debug "

        # Delete the original GLB file
        delete_original_glb_cmd = f" && del {context.scene.Blender2React.R3F_Export_Path}{active_collection.name}.glb "\
            if not context.scene.Blender2React.R3F_Keep_Original_GLB else ''

        # Delete the JSX file created by gltfjsx
        delete_created_jsx_cmd = f" && del {context.scene.Blender2React.R3F_Export_Path}{active_collection.name.capitalize()}.jsx "\
            if not context.scene.Blender2React.R3F_Create_JSX_Component else ''

        # Close the cmd window after 10 seconds
        timeout_and_close_cmd = "&& timeout 10 && exit"

        cmd = glft_jsx_cmd + delete_original_glb_cmd + delete_created_jsx_cmd + timeout_and_close_cmd
        cmd_clean = re.sub(' {2,}', ' ', cmd)
        cmd_clean = cmd_clean.replace("&&", "&&\n")
        cmd_clean = cmd_clean.replace(" --", "\n    --")
        print(cmd_clean + "\n")

        # Change the directory to the export path to run gltfjsx
        # Check if is windows or mac or linux
        print("OPERATING SYSTEM", os.name)
        if os.name == 'nt':
            os.chdir(context.scene.Blender2React.R3F_Export_Path)
            return_code  = subprocess.call(["start", "cmd", "/k", f"{cmd}"], shell=True)
            # process.wait()
        elif os.name == 'posix':
            process = subprocess.Popen(["/bin/bash", "-c", f"{cmd}"])
            process.wait()

        print("collection:", active_collection.name, "exclude:", active_collection.exclude)
        print("-------------------------------------------------------------")
        print("                        EXPORT FINISHED                      ")
        print("_____________________________________________________________")
        print()

        # Move the timeline back to the original frame
        context.scene.frame_set(current_frame)
        context.view_layer.update()

        # Restore the collection status
        # for LayerCollection in context.scene.view_layers[0].layer_collection.children:
        #     LayerCollection.exclude = current_collection_status[LayerCollection.name]

        # Get R3F Project Root and Name from the UI
        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()

        # Move the jsx to components folder
        if return_code == 0:
            # if context.scene.Blender2React.R3F_Create_JSX_Component:
            jsx_path = os.path.join(context.scene.Blender2React.R3F_Export_Path, f"{active_collection.name.capitalize()}.jsx")
            jsx_components_path = os.path.join(R3F_Project_Root, R3F_Project_Name, "src", "components")
            print("jsx_path:", jsx_path)
            print("jsx_components_path:", jsx_components_path)
            os.rename(jsx_path, os.path.join(jsx_components_path, f"{active_collection.name.capitalize()}.jsx"))

        return {'RUNNING_MODAL'}


# Usage
# $ npx gltfjsx [Model.glb] [options]

# Options
#   --output, -o        Output file name/path
# --types, -t         Add Typescript definitions
#   --keepnames, -k     Keep original names
#   --keepgroups, -K    Keep (empty) groups, disable pruning
# --meta, -m          Include metadata (as userData)
#   --shadows, s        Let meshes cast and receive shadows
#   --printwidth, w     Prettier printWidth (default: 120)
# --precision, -p     Number of fractional digits (default: 2)
# --draco, -d         Draco binary path
#   --root, -r          Sets directory from which .gltf file is served
#   --instance, -i      Instance re-occuring geometry
# --instanceall, -I   Instance every geometry (for cheaper re-use)
#   --transform, -T     Transform the asset for the web (draco, prune, resize)
#     --resolution, -R  Transform resolution for texture resizing (default: 1024)
#     --keepmeshes, -j  Do not join compatible meshes
#     --keepmaterials, -M Do not palette join materials
#     --format, -f      Texture format (default: "webp")
#     --simplify, -S    Transform simplification (default: false) (experimental!)
#       --weld          Weld tolerance (default: 0.0001)
#       --ratio         Simplifier ratio (default: 0.075)
#       --error         Simplifier error threshold (default: 0.001)
# --debug, -D         Debug output
