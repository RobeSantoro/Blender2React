import os
import re
import subprocess
import bpy

from .. B2REACT_Globals import get_scene_path, get_project_root, get_project_name


def create_r3f_project(R3F_Project_Root, R3F_Project_Name):
    """Creates a R3F Project in a folder in the given path"""

    print('-------------------------------------------------------')
    print('Executing command in path:', R3F_Project_Root, '\n')

    cmd = f"echo Creating R3F Project in {R3F_Project_Root}...\
            && echo. \
            && cd {R3F_Project_Root}\
            && git clone https://github.com/RobeSantoro/blender2react-template {R3F_Project_Name}\
            && cd {R3F_Project_Name}\
            && git remote rm origin\
            && npm install\
            && timeout 15\
            && exit\
            "

    p = subprocess.Popen(["start", "cmd", "/k", f"{cmd}"], shell=True)
    p.wait()

    cmd_clean = re.sub(' {2,}', ' ', cmd)
    cmd_clean = cmd_clean.replace("&&", "&&\n")
    print(cmd_clean)
    print('-------------------------------------------------------')

    return


class B2REACT_OT_Create_R3F_Project(bpy.types.Operator):
    """Creates a R3F Project in a folder next to the current blender file if no path is given"""

    bl_idname = "blender2react.create_r3f_project"
    bl_label = "Create R3F Project next to the current blender file?"

    bl_description = "Creates a R3F Project in a folder next to the current blender file"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        Scene_Path = get_scene_path()
        if Scene_Path is None:
            return {"CANCELLED"}

        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()

        if R3F_Project_Root == "":
            print("No R3F Project Path given")
            self.report({"ERROR"}, "No R3F Project Path given")
            return {"CANCELLED"}

        # Create R3F Project
        create_r3f_project(R3F_Project_Root, R3F_Project_Name)

        # Setting Initialized
        bpy.context.scene.Blender2React.R3F_Initialized = True

        # Setting Export Path
        bpy.context.scene.Blender2React.R3F_Export_Path = os.path.join(
            R3F_Project_Root, R3F_Project_Name, "public"
        )

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)
