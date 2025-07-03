import os
import platform
import subprocess
import bpy

from .. B2REACT_Globals import get_scene_path, get_project_root, get_project_name


class B2REACT_OT_StartDevServer(bpy.types.Operator):

    bl_label = "Start Dev Server"
    bl_idname = "blender2react.start_dev_server"

    bl_description = "Starts the dev server for the current R3F Project"
    bl_options = {"REGISTER"}

    bl_category = "Blender2React"

    def execute(self, context):
        platform_system = platform.system()

        print('-------------------------------------------------------')
        print('----------------- Starting Dev Server -----------------')
        print('-------------------------------------------------------')
        print()

        project_location = os.path.join(get_project_root(), get_project_name())

        os.chdir(project_location)

        if platform_system == "Windows":
            cmd = f"cd {project_location} && npm run dev"
            p = subprocess.Popen(["start", "cmd", "/k", f"{cmd}"], shell=True)
            p.wait()
        elif platform_system == "Darwin":
            # Launch a new Terminal window and run npm run dev in the project location
            command = f'cd \\"{project_location}\\" && npm run dev'
            apple_script = f'tell application "Terminal" to do script "{command}"'
            subprocess.Popen([
                "osascript",
                "-e",
                apple_script
            ])
        elif platform_system == "Linux":
            pass

        print('-------------------------------------------------------')
        return {'FINISHED'}
