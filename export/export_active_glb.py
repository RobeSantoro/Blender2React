import os
import re
import subprocess
import bpy

from bpy_extras.io_utils import ExportHelper

from . export_glb import export_glb
from .. B2REACT_Globals import get_project_root, get_project_name, get_export_path


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

        if (context.view_layer.active_layer_collection is None
                or context.view_layer.active_layer_collection.name == "Scene Collection"
                ):
            print("WARNING: No Active Collection selected.")
            self.report({'ERROR'}, "No Active Collection selected.")
            return {'CANCELLED'}

        # Convert relative path to absolute path if //
        if context.scene.Blender2React.R3F_Export_Path.startswith("//"):
            context.scene.Blender2React.R3F_Export_Path = bpy.path.abspath(context.scene.Blender2React.R3F_Export_Path)

        # Get the actual frame number and Move the timeline to the last frame
        # to avoid animation issues (scale = 0
        current_frame = context.scene.frame_current
        context.scene.frame_set(context.scene.frame_end)
        context.view_layer.update()

        print()
        print("-------------------------------------------------------------")
        print("-------------- EXPORT ACTIVE COLLECTION AS GLB --------------")
        print("-------------------------------------------------------------")
        print()

        # Set the filepath from the export path and the collection name
        active_collection = context.view_layer.active_layer_collection
        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()
        R3F_Export_Path = get_export_path()
        filepath = os.path.join(R3F_Export_Path, active_collection.name)
        output_path = os.path.join(
            R3F_Project_Root,
            R3F_Project_Name,
            "src\\",
            "components\\",
            active_collection.name.capitalize())
        components_path = os.path.join(
            R3F_Project_Root,
            R3F_Project_Name,
            "src\\",
            "components\\")
        export_folder = os.path.basename(os.path.normpath(R3F_Export_Path))

        print("active_collection:", active_collection.name)
        print("R3F_Project_Name: ", R3F_Project_Name)
        print("R3F_Project_Root: ", R3F_Project_Root)
        print("R3F_Export_Path:  ", R3F_Export_Path)
        print("filepath:         ", filepath)
        print("output_path:      ", output_path)
        print("export_folder:    ", export_folder)
        print()

        # Export the GLB file
        export_glb(filepath, active=True)

        # Launch gltfjsx command cd {context.scene.Blender2React.R3F_Export_Path} &&\
        glft_jsx_cmd = f"\
                npx gltfjsx {filepath}.glb\
                --output {output_path}.jsx\
                --keepnames\
                --keepgroups\
                --instance\
                --printwidth 80\
                --root {R3F_Export_Path}\
                --transform\
                --shadows\
                --debug "

        # Delete the original GLB file
        delete_original_glb_cmd = f" && del {R3F_Export_Path}{active_collection.name}.glb "\
            if not context.scene.Blender2React.R3F_Keep_Original_GLB else ''

        # Delete the JSX file created by gltfjsx
        delete_created_jsx_cmd = f" && del {R3F_Export_Path}{active_collection.name.capitalize()}.jsx "\
            if not context.scene.Blender2React.R3F_Create_JSX_Component else ''

        # Close the cmd window after 10 seconds && timeout 10
        timeout_and_close_cmd = "&& exit"

        cmd = glft_jsx_cmd + delete_original_glb_cmd + delete_created_jsx_cmd + timeout_and_close_cmd
        cmd_clean = re.sub(' {2,}', ' ', cmd)
        cmd_clean = cmd_clean.replace("&&", "&&\n")
        cmd_clean = cmd_clean.replace(" --", "\n    --")
        print(cmd_clean + "\n")

        # Change the directory to the export path to run gltfjsx
        # Check if is windows or mac or linux
        print("OPERATING SYSTEM", os.name)
        if os.name == 'nt':
            os.chdir(R3F_Export_Path)
            process = subprocess.run(["start", "cmd", "/k", f"{cmd}"],
                                     shell=True,
                                     capture_output=True,
                                     text=True
                                     )
            print(process.stdout)
        elif os.name == 'posix':
            process = subprocess.Popen(["/bin/bash", "-c", f"{cmd}"])
            process.wait()

        print("collection:", active_collection.name, "exclude:", active_collection.exclude)
        print("_____________________________________________________________")
        print("                        EXPORT FINISHED                      ")
        print("_____________________________________________________________")
        print()

        # Move the timeline back to the original frame
        context.scene.frame_set(current_frame)
        context.view_layer.update()

        if context.scene.Blender2React.R3F_Create_JSX_Component:

            # Move the jsx to components folder
            try:
                os.rename(
                    f"{filepath}.jsx",
                    f"{output_path}.jsx"
                )
            except FileExistsError as err:
                print("File already exists.")
                self.report({'ERROR'}, "File already exists.")
                bpy.context.window_manager.popup_menu(
                    lambda self, context:
                        self.layout.label(text=str(err)),
                    title="Error moving some files.",
                    icon='ERROR')
                return {'CANCELLED'}

            # Open the jsx file and modify component name and path
            # with open(f"{output_path}.jsx", 'r') as jsx_file:

            #     jsx_file_data = jsx_file.read()

            #     # ...replace the string 'export function Model' with 'export default function collection.name'
            #     jsx_file_data = jsx_file_data.replace(
            #         "export function Model",
            #         f'export default function {active_collection.name.capitalize()}'
            #     )

            #     # ...replace the string '/active_collection.name-transformed.glb' to '/export_folder/active_collection.name-transformed.glb'
            #     jsx_file_data = jsx_file_data.replace(
            #         f'/{active_collection.name}-transformed.glb',
            #         f'/{export_folder}/{active_collection.name}-transformed.glb'
            #     )

            # with open(f"{output_path}.jsx", 'w') as jsx_file:
            #     jsx_file.write(jsx_file_data)

            # # Add the import statement to the World.js file
            # with open(f"{components_path}World.jsx", 'r') as world_file:

            #     world_file_data = world_file.read()

            #     # Add the import statement at the beginning of the World.js file
            #     world_file.seek(0, 0)
            #     world_file_data = f"import {active_collection.name.capitalize()} from './{active_collection.name.capitalize()}.jsx';\n" + world_file_data

            # # Write the new World.js file
            # with open(f"{components_path}World.jsx", 'w') as world_file:
            #     world_file.write(world_file_data)

            # # Add the component to the scene inside the fragment tag
            # pattern = r"<>\n(.*?)</>"
            # match = re.search(pattern, world_file_data, re.DOTALL)

            # if match:
            #     fragment = match.group()
            #     print(fragment)
            #     with open(f"{components_path}World.jsx", 'w') as world_file:
            #         world_file.write(world_file_data.replace(fragment, f"<>\n<{active_collection.name.capitalize()} />\n</>"))

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
