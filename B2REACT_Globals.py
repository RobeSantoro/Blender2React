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


def get_export_path():
    """ Get the export path from
    bpy.context.scene.Blender2React.R3F_Export_Path.
    If not set, it will be set to the path of the current file.
    """

    if bpy.context.scene.Blender2React.R3F_Export_Path == "":

        bpy.context.window_manager.popup_menu(
            lambda self, context:
                self.layout.label(text="No Export Path set."),
                title="No Export Path set!",
                icon='ERROR')

    return bpy.context.scene.Blender2React.R3F_Export_Path


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

    #############################
    # GLTF 2 JSX EXPORT OPTIONS #
    #############################

    R3F_JSX_types: bpy.props.BoolProperty(
        name="types",
        description="Add types to the JSX Component",
        default=False,
    )

    R3F_JSX_keepnames: bpy.props.BoolProperty(
        name="JSX_keepnames",
        description="Keep the original names of the objects in the JSX Component",
        default=True,
    )

    R3F_JSX_keepgroups: bpy.props.BoolProperty(
        name="JSX_keepgroups",
        description="Keep the original groups of the objects in the JSX Component",
        default=True,
    )

    R3F_JSX_shadows: bpy.props.BoolProperty(
        name="JSX_shadows",
        description="Add cast nd receive shadows props to the JSX Component",
        default=True,
    )

    R3F_JSX_printwidth: bpy.props.IntProperty(
        name="printwidth",
        description="Set the printwidth for the JSX Component",
        default=120,
    )

    R3F_JSX_precision: bpy.props.IntProperty(
        name="precision",
        description="Set the precision for the JSX Component",
        default=2,
    )

    R3F_JSX_instance: bpy.props.BoolProperty(
        name="JSX_instance",
        description="Use instances instead of copies in the JSX Component and GLB",
        default=True,
    )

    R3F_JSX_transform: bpy.props.BoolProperty(
        name="JSX_transform",
        description="Optimize the asset for the web (draco, prune, resize)",
        default=True,
    )

    R3F_JSX_debug: bpy.props.BoolProperty(
        name="JSX_debug",
        description="Debug the JSX Component",
        default=True,
    )

    #############################@
    # OPERATIONS AFTER EXPORTING #
    #############################@

    R3F_Delete_Original_GLB: bpy.props.BoolProperty(
        name="Delete_Original_GLB",
        description="Delete the original GLB after exporting",
        default=True,
    )

    R3F_Delete_JSX_Component: bpy.props.BoolProperty(
        name="Delete_JSX_Component",
        description="Delete the JSX Component after exporting",
        default=False,
    )