import bpy

from . B2REACT_Globals import B2REACT_Globals

# # User Interface
from . B2REACT_UI import B2REACT_PT_Init_Panel
# from . B2REACT_UI import B2REACT_PT_Edit_Panel
# from . B2REACT_UI import B2REACT_PT_Utils_Panel
# from . B2REACT_UI import B2REACT_PT_Export_Panel

# Initialization
from . init.create_r3f_project import B2REACT_OT_Create_R3F_Project
from . init.start_dev_server import B2REACT_OT_StartDevServer
from . init.open_vscode import B2REACT_OT_Open_Project_in_VSCode
from . init.open_folder import B2REACT_OT_open_project_folder

# # Edit React Template
# from . edit.edit_template import B2REACT_OT_Edit_Template

# # Utilities
# from . utils.pushdown_actions import B2REACT_OT_PushDownActons
# from . utils.rename_tracks import R3F_OT_RenameTracks
# from . utils.rename_geo import R3F_OT_RenameGeo

# # Export
# from . export.export_all_glb import R3F_OT_ExportAll_GLB
# from . export.export_active_glb import R3F_OT_ExportActive_GLB


bl_info = {
    "name": "Blender 2 React",
    "author": "Robe Santoro",
    "description": "Work in Progress",
    "blender": (3, 6, 0),
    "version": (0, 0, 1),
    "location": "View3D > UI > Blender 2 React",
    "category": "Blender2React"
}


def register():

    bpy.utils.register_class(B2REACT_Globals)
    bpy.types.Scene.Blender2React = bpy.props.PointerProperty(type=B2REACT_Globals)

    bpy.utils.register_class(B2REACT_PT_Init_Panel)
    # bpy.utils.register_class(B2REACT_PT_Edit_Panel)
    # bpy.utils.register_class(B2REACT_PT_Utils_Panel)
    # bpy.utils.register_class(B2REACT_PT_Export_Panel)

    bpy.utils.register_class(B2REACT_OT_Create_R3F_Project)
    bpy.utils.register_class(B2REACT_OT_StartDevServer)
    bpy.utils.register_class(B2REACT_OT_Open_Project_in_VSCode)
    bpy.utils.register_class(B2REACT_OT_open_project_folder)

    # bpy.utils.register_class(B2REACT_OT_Edit_Template)

    # bpy.utils.register_class(B2REACT_OT_PushDownActons)
    # bpy.utils.register_class(R3F_OT_RenameTracks)
    # bpy.utils.register_class(R3F_OT_RenameGeo)

    # bpy.utils.register_class(R3F_OT_ExportAll_GLB)
    # bpy.utils.register_class(R3F_OT_ExportActive_GLB)


def unregister():

    bpy.utils.unregister_class(B2REACT_PT_Init_Panel)
    # bpy.utils.unregister_class(B2REACT_PT_Edit_Panel)
    # bpy.utils.unregister_class(B2REACT_PT_Utils_Panel)
    # bpy.utils.unregister_class(B2REACT_PT_Export_Panel)

    bpy.utils.unregister_class(B2REACT_OT_Create_R3F_Project)
    bpy.utils.unregister_class(B2REACT_OT_StartDevServer)
    bpy.utils.unregister_class(B2REACT_OT_Open_Project_in_VSCode)
    bpy.utils.unregister_class(B2REACT_OT_open_project_folder)

    # bpy.utils.unregister_class(B2REACT_OT_Edit_Template)

    # bpy.utils.unregister_class(B2REACT_OT_PushDownActons)
    # bpy.utils.unregister_class(R3F_OT_RenameTracks)
    # bpy.utils.unregister_class(R3F_OT_RenameGeo)

    # bpy.utils.unregister_class(R3F_OT_ExportAll_GLB)
    # bpy.utils.unregister_class(R3F_OT_ExportActive_GLB)

    bpy.utils.unregister_class(B2REACT_Globals)
    del bpy.types.Scene.Blender2React


if __name__ == "__main__":
    register()
