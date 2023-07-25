import bpy
import os
import subprocess

from .. B2REACT_Globals import get_scene_path, get_project_root, get_project_name


class B2REACT_OT_StartDevServer(bpy.types.Operator):

    bl_label = "Start Dev Server"
    bl_idname = "blender2react.start_dev_server"

    bl_description = "Starts the dev server for the current R3F Project"
    bl_options = {"REGISTER"}

    bl_category = "Blender2React"

    def execute(self, context):
        print('_______________________________________________________')
        print("Starting Dev Server...")
        print('-------------------------------------------------------')

        project_location = get_project_root() + "\\" + get_project_name()

        os.chdir(project_location)

        # Launch gltfjsx command to compress the GLB file
        # and delete the Animation.jsx and animation.glb files
        cmd = f"cd {project_location} && npm run dev"

        p = subprocess.Popen(["start", "cmd", "/k", f"{cmd}"], shell=True)
        p.wait()

        # Open the browser to the localhost
        # cmd = f"start chrome http://127.0.0.1:5173/"
        # os.system(cmd)

        return {'FINISHED'}
