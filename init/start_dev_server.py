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

        project_location = os.path.join(get_project_root(), get_project_name())

        os.chdir(project_location)
        cmd = f"cd {project_location} && npm run dev"
        p = subprocess.Popen(["start", "cmd", "/k", f"{cmd}"], shell=True)
        p.wait()

        print('_______________________________________________________')
        return {'FINISHED'}
