import os
import bpy

from .. B2REACT_Globals import get_project_root, get_project_name


class B2REACT_OT_Open_Project_in_VSCode(bpy.types.Operator):
    """Opens the current R3F Project in VSCode"""

    bl_idname = "blender2react.open_project_in_vscode"
    bl_label = "Open VS Code"

    bl_description = "Opens the current R3F Project in VS Code"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        project_location = get_project_root() + "\\" + get_project_name()

        print("project_location:", project_location)

        cmd = 'code ' + project_location

        if project_location != "":
            os.system(cmd)
        else:
            self.report({"ERROR"}, "No Project Path set")

        return {"FINISHED"}
