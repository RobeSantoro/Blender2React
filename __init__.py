import bpy

from . B2R3F_Globals import B2R3F_Globals

# # User Interface
from . B2R3F_UI import B2R3F_PT_Init_Panel
# from . B2R3F_UI import B2DREI_PT_Edit_Panel
# from . B2R3F_UI import B2DREI_PT_Utils_Panel
# from . B2R3F_UI import B2DREI_PT_Export_Panel

# # Initialization
# from . init.init_r3f_project import B2DREI_OT_Init_R3F_Project
# from . init.start_dev_server import B2DREI_OT_StartDevServer
# from . init.open_vscode import B2DREI_OT_Open_Project_in_VSCode
# from . init.open_folder import B2DREI_OT_Open_Project_in_Explorer

# # Edit React Template
# from . edit.edit_template import B2DREI_OT_Edit_Template

# # Utilities
# from . utils.pushdown_actions import B2DREI_OT_PushDownActons
# from . utils.rename_tracks import R3F_OT_RenameTracks
# from . utils.rename_geo import R3F_OT_RenameGeo

# # Export
# from . export.export_all_glb import R3F_OT_ExportAll_GLB
# from . export.export_active_glb import R3F_OT_ExportActive_GLB


bl_info = {
    "name": "Blender 2 R3F",
    "author": "Robe Santoro",
    "description": "Work in Progress",
    "blender": (3, 6, 0),
    "version": (0, 0, 1),
    "location": "View3D > UI > Blender2R3F",
    "category": "Blender2R3F"
}


def register():

    bpy.utils.register_class(B2R3F_PT_Init_Panel)
    # bpy.utils.register_class(B2DREI_PT_Edit_Panel)
    # bpy.utils.register_class(B2DREI_PT_Utils_Panel)
    # bpy.utils.register_class(B2DREI_PT_Export_Panel)

    # bpy.utils.register_class(B2DREI_OT_Init_R3F_Project)
    # bpy.utils.register_class(B2DREI_OT_StartDevServer)
    # bpy.utils.register_class(B2DREI_OT_Open_Project_in_VSCode)
    # bpy.utils.register_class(B2DREI_OT_Open_Project_in_Explorer)

    # bpy.utils.register_class(B2DREI_OT_Edit_Template)

    # bpy.utils.register_class(B2DREI_OT_PushDownActons)
    # bpy.utils.register_class(R3F_OT_RenameTracks)
    # bpy.utils.register_class(R3F_OT_RenameGeo)

    # bpy.utils.register_class(R3F_OT_ExportAll_GLB)
    # bpy.utils.register_class(R3F_OT_ExportActive_GLB)

    bpy.utils.register_class(B2R3F_Globals)
    bpy.types.Scene.Blender2R3F = bpy.props.PointerProperty(type=B2R3F_Globals)


def unregister():

    # bpy.utils.unregister_class(B2DREI_PT_Init_Panel)
    # bpy.utils.unregister_class(B2DREI_PT_Edit_Panel)
    # bpy.utils.unregister_class(B2DREI_PT_Utils_Panel)
    # bpy.utils.unregister_class(B2DREI_PT_Export_Panel)

    # bpy.utils.unregister_class(B2DREI_OT_Init_R3F_Project)
    # bpy.utils.unregister_class(B2DREI_OT_StartDevServer)
    # bpy.utils.unregister_class(B2DREI_OT_Open_Project_in_VSCode)
    # bpy.utils.unregister_class(B2DREI_OT_Open_Project_in_Explorer)

    # bpy.utils.unregister_class(B2DREI_OT_Edit_Template)

    # bpy.utils.unregister_class(B2DREI_OT_PushDownActons)
    # bpy.utils.unregister_class(R3F_OT_RenameTracks)
    # bpy.utils.unregister_class(R3F_OT_RenameGeo)

    # bpy.utils.unregister_class(R3F_OT_ExportAll_GLB)
    # bpy.utils.unregister_class(R3F_OT_ExportActive_GLB)

    bpy.utils.unregister_class(B2R3F_Globals)
    del bpy.types.Scene.Blender2R3F


if __name__ == "__main__":
    register()
