import os
import bpy
import platform

from .. B2REACT_Globals import get_project_root, get_project_name


class B2REACT_OT_open_project_folder(bpy.types.Operator):
    """Opens the current R3F Project folder"""

    bl_idname = "blender2react.open_project_folder"
    bl_label = "Open Folder"

    bl_description = "Opens the current R3F Project folder"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        print('-------------------------------------------------------')
        print("Opening Project Folder...")

        project_location = os.path.join(get_project_root(), get_project_name())
        platform_system = platform.system()

        if project_location == "":
            print("No Project Path set")
            self.report({"ERROR"}, "No Project Path set")
            return {"CANCELLED"}

        print("platform_system:", platform_system)
        print("project_location:", project_location)

        if platform_system == "Windows":
            cmd = f'explorer.exe "{project_location}"'
            print("command:", cmd)
            os.system(cmd)
        elif platform_system == "Darwin":
            cmd = f'open "{project_location}"'
            print("Command:", cmd)
            os.system(cmd)
        elif platform_system == "Linux":
            pass

        print('------------------------------------------------------')
        print
        return {"FINISHED"}
