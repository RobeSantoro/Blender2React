import os
import stat
import shutil
import bpy

from .. B2REACT_Globals import get_project_root, get_project_name


def remove_readonly(fn, path, excinfo):
    """Remove read only files"""

    try:
        os.chmod(path, stat.S_IWRITE)
        fn(path)
        print('Deleting Project Files')

    except Exception as exc:
        bpy.context.window_manager.popup_menu(
            lambda self, context:
                self.layout.label(text=str(exc)),
                title="Error deleting some files.",
                icon='ERROR')
        print("Skipped:", path, "because:\n", exc)


class B2REACT_OT_Delete_R3F_Project(bpy.types.Operator):
    """Delete the R3F Project and reset the Blender2React Addon"""

    bl_idname = "blender2react.delete_r3f_project"
    bl_label = "Resetting Blender2React will DEELTE the project folder."

    bl_description = "Delete the R3F Project and reset the Blender2React Addon"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()

        project_path = os.path.join(R3F_Project_Root, R3F_Project_Name)

        print('-------------------------------------------------------')
        print('Deleting Project Folder:', project_path)

        # If exists
        if os.path.exists(project_path):

            # Delete Project folder
            shutil.rmtree(project_path, onerror=remove_readonly)

            # Reset Globals
            context.scene.Blender2React.Scene_Path = ""
            context.scene.Blender2React.R3F_Project_Root = ""
            context.scene.Blender2React.R3F_Project_Name = ""
            context.scene.Blender2React.R3F_Initialized = False
            context.scene.Blender2React.R3F_Project_Title = ""
            context.scene.Blender2React.R3F_Export_Name = ""
            context.scene.Blender2React.R3F_Export_Path = ""
            context.scene.Blender2React.R3F_Keep_Original_GLB = False
            context.scene.Blender2React.R3F_Create_JSX_Component = True

            print('Blender2React Add-on Set to default values')
            print('_______________________________________________________')

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)
