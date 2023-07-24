import os
import bpy

# from .. B2DREI_Globals import get_project_root, get_project_name


class B2DREI_OT_Open_Project_in_Explorer(bpy.types.Operator):
    """Opens the current R3F Project in Explorer"""

    bl_idname = "Blender2R3F.open_project_folder"
    bl_label = "Open Project in Explorer"

    bl_description = "Opens the current R3F Project in Explorer"
    bl_options = {"REGISTER"}
    bl_category = "Blender2R3F"

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
