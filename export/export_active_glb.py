import os
import re
import shutil
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
            context.scene.Blender2React.R3F_Export_Path = (
                bpy.path.abspath(context.scene.Blender2React.R3F_Export_Path)
            )

        # Get the actual frame number and Move the timeline to the last frame
        # to avoid animation issues (scale = 0
        # current_frame = context.scene.frame_current
        # context.scene.frame_set(context.scene.frame_end)
        # context.view_layer.update()

        print()
        print("-------------------------------------------------------------")
        print("-------------- EXPORT ACTIVE COLLECTION AS GLB --------------")
        print("-------------------------------------------------------------")
        print()

        # Set the filepath from the export path and the collection name
        active_collection = context.view_layer.active_layer_collection
        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()

        jsx_output_path = os.path.join(
            R3F_Project_Root,
            R3F_Project_Name,
            "src\\",
            "components\\",
            active_collection.name.capitalize())

        R3F_Export_Path = get_export_path()
        glb_filepath = os.path.join(R3F_Export_Path, active_collection.name)

        public_folder = os.path.basename(os.path.normpath(R3F_Export_Path))

        print("active_collection:", active_collection.name)
        # print("R3F_Project_Name: ", R3F_Project_Name)
        # print("R3F_Project_Root: ", R3F_Project_Root)
        print("R3F_Export_Path:  ", R3F_Export_Path)
        print("glb_filepath:     ", glb_filepath)
        print("jsx_output_path:  ", jsx_output_path)
        print("public_folder:    ", public_folder)
        print()

        # Check if the export path exists
        # TODO ALl this kind of check should be done
        # in the get functions in B2REACT_Globals.py
        if not os.path.exists(R3F_Export_Path):
            print("WARNING: R3F_Export_Path does not exist.")
            self.report({'ERROR'}, "R3F_Export_Path does not exist.")
            return {'CANCELLED'}

        # Export the GLB file
        try:
            export_glb(glb_filepath, active_collection=True)
        except:
            print("WARNING: No GLB file found.")
            self.report({'ERROR'}, "No GLB file found.")
            return {'CANCELLED'}

        # Launch gltfjsx command cd {context.scene.Blender2React.R3F_Export_Path} &&\
        glft_jsx_cmd = f"\
                npx gltfjsx {glb_filepath}.glb\
                --output {jsx_output_path}.jsx\
                {'--types' if context.scene.Blender2React.R3F_JSX_typescript else ''}\
                {'--keepnames' if context.scene.Blender2React.R3F_JSX_keepnames else ''}\
                {'--keepgroups' if context.scene.Blender2React.R3F_JSX_keepgroups else ''}\
                {'--shadows' if context.scene.Blender2React.R3F_JSX_shadows else ''}\
                --printwidth {context.scene.Blender2React.R3F_JSX_printwidth}\
                --precision {context.scene.Blender2React.R3F_JSX_precision}\
                --exportdefault\
                --root {R3F_Export_Path}\
                {'--transform' if context.scene.Blender2React.R3F_JSX_transform else ''}\
                    {'--instance' if context.scene.Blender2React.R3F_JSX_instance and context.scene.Blender2React.R3F_JSX_transform else ''}\
                    {f'--resolution {context.scene.Blender2React.R3F_JSX_resolution}' if context.scene.Blender2React.R3F_JSX_transform else ''}\
                    {'--keepmeshes' if context.scene.Blender2React.R3F_JSX_keepmeshes and context.scene.Blender2React.R3F_JSX_transform else ''}\
                    {'--keepmaterials' if context.scene.Blender2React.R3F_JSX_keepmaterials and context.scene.Blender2React.R3F_JSX_transform else ''}\
                    {f'--format {context.scene.Blender2React.R3F_JSX_format}' if context.scene.Blender2React.R3F_JSX_transform else ''}\
                {'--debug' if context.scene.Blender2React.R3F_JSX_debug else ''}\
                "

        # Delete the JSX file created by gltfjsx
        delete_created_jsx_cmd = f" && del {jsx_output_path}.jsx "\
            if context.scene.Blender2React.R3F_Delete_JSX_Component else ''

        # Delete the original GLB file
        delete_original_glb_cmd = f" && del {glb_filepath}.glb "\
            if context.scene.Blender2React.R3F_Delete_Original_GLB else ''

        # Close the cmd window after 10 seconds
        timeout_and_close_cmd = "&& timeout 15 && exit"

        cmd = (
            glft_jsx_cmd +
            delete_original_glb_cmd +
            delete_created_jsx_cmd +
            timeout_and_close_cmd
        )

        # Clean the cmd string to print it in the console
        cmd_clean = re.sub(' {2,}', ' ', cmd)
        cmd_clean = cmd_clean.replace("&&", "&&\n")
        cmd_clean = cmd_clean.replace(" --", "\n    --")
        print(cmd_clean + "\n")

        # Check if is windows or mac or linux
        print("OPERATING SYSTEM", os.name)
        if os.name == 'nt':
            try:  # Check if npx is installed
                process = subprocess.run(["npx", "-v"],
                                         shell=True,
                                         capture_output=True,
                                         text=True
                                         )
                print("npx version:", process.stdout)

            except:  # If not, install it with npm i -g npx\
                process = subprocess.run(["npm", "i", "-g", "npx"],
                                         shell=True,
                                         capture_output=True,
                                         text=True
                                         )
                print("npx version:", process.stdout)

            # Change the directory to the export path to run gltfjsx
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

        print()
        print("-------------------------------------------------------------")
        print("                        EXPORT FINISHED                      ")
        print("_____________________________________________________________")
        print()

        bpy.context.window_manager.popup_menu(
            lambda self, context: self.layout.label(text="Export finished."),
            title="Export finished.",
            icon='INFO')

        # Move the timeline back to the original frame
        # context.scene.frame_set(current_frame)
        # context.view_layer.update()

        # Open the jsx file and modify component name and path
        if not context.scene.Blender2React.R3F_Delete_JSX_Component:

            # On some system gltf2jsx fails to create the jsx file into the output_path
            # so we need to check if the file exists before trying to open it
            # and if not, we need to move it from the `filepath` to the `output_path`
            if not os.path.exists(f"{jsx_output_path}.jsx"):
                print("WARNING: JSX file not found in the output path.")
                shutil.move(f"{glb_filepath}.jsx", f"{jsx_output_path}.jsx")
                print("JSX file moved from filepath to output_path.")

            with open(f"{jsx_output_path}.jsx", 'r') as jsx_file:

                jsx_file_data = jsx_file.read()

                # ...replace the string 'export function Model'
                # with 'export default function collection.name'
                jsx_file_data = jsx_file_data.replace(
                    "export default function Model",
                    f'export default function {active_collection.name.capitalize()}'
                )

                # ...replace the string '/active_collection.name-transformed.glb'
                # to '/export_folder/active_collection.name-transformed.glb'

                # if context.scene.Blender2React.R3F_JSX_transform and export_folder != 'public':
                #     jsx_file_data = jsx_file_data.replace(
                #         f'/{active_collection.name}-transformed.glb',
                #         f'/{export_folder}/{active_collection.name}-transformed.glb'

                #     )

            with open(f"{jsx_output_path}.jsx", 'w') as jsx_file:
                jsx_file.write(jsx_file_data)

        # Move the jsx to components folder because gltfjsx does not use the output param correctly
        # if not context.scene.Blender2React.R3F_Delete_JSX_Component:

        #     # Move the jsx to components folder
        #     try:
        #         os.rename(
        #             f"{filepath}.jsx",
        #             f"{output_path}.jsx"
        #         )
        #     except FileExistsError as err:
        #         print("File already exists.")
        #         self.report({'ERROR'}, "File already exists. Cannot move jsx file.")
        #         bpy.context.window_manager.popup_menu(
        #             lambda self, context:
        #                 self.layout.label(text=str(err)),
        #             title="File already exists. Cannot move jsx file.",
        #             icon='ERROR')
        #         return {'CANCELLED'}

        return {'RUNNING_MODAL'}


# Usage
# $ npx gltfjsx [Model.glb] [options]

# Options
# --output, -o             Output file name/path                                                +
# --types, -t              Add Typescript definitions                                           +
# --keepnames, -k          Keep original names                                                  +
# --keepgroups, -K         Keep (empty) groups, disable pruning                                 +
# --meta, -m               Include metadata (as userData)
# --shadows, s             Let meshes cast and receive shadows                                  +
# --printwidth, w          Prettier printWidth (default: 120)                                   +
# --precision, -p          Number of fractional digits (default: 2)                             +
# --draco, -d              Draco binary path
# --root, -r               Sets directory from which .gltf file is served                       +
# --instance, -i           Instance re-occuring geometry                                        +
# --instanceall, -I        Instance every geometry (for cheaper re-use)
# --exportdefault, -E      Use default export 
# --transform, -T          Transform the asset for the web (draco, prune, resize)               +
#   --resolution, -R           Transform resolution for texture resizing (default: 1024)        +      
#   --keepmeshes, -j           Do not join compatible meshes                                    +
#   --keepmaterials, -M        Do not palette join materials                                    +
#   --format, -f               Texture format (default: "webp")                                 +
#   --simplify, -S             Transform simplification (default: false) (experimental!)        
#     --weld                        Weld tolerance (default: 0.0001)
#     --ratio                       Simplifier ratio (default: 0.075)
#     --error                       Simplifier error threshold (default: 0.001)
# --debug, -D              Debug output                                                         +