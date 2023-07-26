import bpy


def get_scene_path():
    """ Get the path of the current file and updates Blender2React.Scene_Path"""

    # Check if the current file is saved
    if len(bpy.path.abspath("//")) <= 0 or bpy.data.is_saved is False:

        print("Scene Path not found. Save Blender file first.")

        bpy.context.window_manager.popup_menu(
            lambda self, context:
                self.layout.label(text="Scene Path not found. Save Blender file first."),
                title="Save Blender File first!",
                icon='ERROR')

        return None

    # Get the path of the current file
    current_path = bpy.path.abspath("//")

    bpy.context.scene.Blender2React.Scene_Path = current_path
    return bpy.context.scene.Blender2React.Scene_Path


def get_project_root():
    """ Get the root of the R3F Project from
    bpy.context.scene.Blender2React.R3F_Project_Root.
    If not set, it will be set to the path of the current file.
    """

    if bpy.context.scene.Blender2React.R3F_Project_Root == "":

        Project_Path = get_scene_path()
        bpy.context.scene.Blender2React.R3F_Project_Root = Project_Path

    return bpy.context.scene.Blender2React.R3F_Project_Root


def get_project_name():
    """ Get the name of the R3F Project from
    bpy.context.scene.Blender2React.R3F_Project_Name.
    If not set, it will be set to "r3f-project
    """

    if bpy.context.scene.Blender2React.R3F_Project_Name == "":
        bpy.context.scene.Blender2React.R3F_Project_Name = "r3f-project"

    return bpy.context.scene.Blender2React.R3F_Project_Name


def get_project_title():

    if bpy.context.scene.Blender2React.R3F_Project_Title == "":
        bpy.context.scene.Blender2React.R3F_Project_Title = get_project_name()

    return bpy.context.scene.Blender2React.R3F_Project_Title


class B2REACT_Globals(bpy.types.PropertyGroup):

    Scene_Path: bpy.props.StringProperty(
        name="Scene_Path",
        description="Path to the Scene",
        default="",
        maxlen=1024,
        subtype='DIR_PATH',
    )

    R3F_Project_Root: bpy.props.StringProperty(
        name="R3F_Project_Root",
        description="Root of the R3F Project",
        default="",
        maxlen=1024,
        subtype='DIR_PATH',
    )

    R3F_Project_Name: bpy.props.StringProperty(
        name="R3F_Project_Name",
        description="Name of the R3F Project",
        default="",
        maxlen=1024,
    )

    R3F_Initialized: bpy.props.BoolProperty(
        name="R3F_Initialized",
        description="Is the R3F Project Initialized",
        default=False,
    )

    R3F_Project_Title: bpy.props.StringProperty(
        name="R3F_Project_Title",
        description="Title of the R3F Project",
        default="",
        maxlen=1024,
    )

    R3F_Export_Name: bpy.props.StringProperty(
        name="R3F_Export_Name",
        description="Name of the R3F Componeent Export",
        default="",
        maxlen=1024,
    )

    R3F_Export_Path: bpy.props.StringProperty(
        name="R3F_Export_Path",
        description="Path to the R3F Collection Export",
        default="",
        maxlen=1024,
        subtype='DIR_PATH',
    )

    R3F_Keep_Original_GLB: bpy.props.BoolProperty(
        name="Keep_Original_GLB",
        description="Keep the original GLB file after exporting",
        default=False,
    )

    R3F_Create_JSX_Component: bpy.props.BoolProperty(
        name="Create_JSX_Component",
        description="Create a JSX Component for the exported GLB",
        default=True,
    )
