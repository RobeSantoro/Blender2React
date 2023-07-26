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

        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()
        
        project_location = os.path.join(R3F_Project_Root, R3F_Project_Name)

        print("project_location:", project_location)

        if project_location:
            self.report({"INFO"}, "Opening VS Code")
            print("Opening VS Code")
            cmd = f'code "{project_location}"'
            os.system(cmd)            
        else:
            self.report({"ERROR"}, "No Project Path set")
            print("No Project Path set")

        return {"FINISHED"}
