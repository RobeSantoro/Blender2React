import bpy


class B2R3F_Globals(bpy.types.PropertyGroup):

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

    R3F_Project_Title: bpy.props.StringProperty(
        name="R3F_Project_Title",
        description="Title of the R3F Project",
        default="",
        maxlen=1024,
    )

    R3F_Export_Name: bpy.props.StringProperty(
        name="R3F_Export_Name",
        description="Name of the R3F Componeent Export",
        default="animation",
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
