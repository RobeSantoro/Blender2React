import os
import bpy

from .. B2REACT_Globals import get_project_root, get_project_name


class B2REACT_OT_open_project_folder(bpy.types.Operator):
    """Opens the current R3F Project in Explorer"""

    bl_idname = "blender2react.open_project_folder"
    bl_label = "Open Project in Explorer"

    bl_description = "Opens the current R3F Project in Explorer"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        project_location = get_project_root() + get_project_name()

        print("project_location:", project_location)

        cmd = 'explorer.exe ' + project_location

        if project_location != "":
            os.system(cmd)
        else:
            self.report({"ERROR"}, "No Project Path set")

        return {"FINISHED"}
