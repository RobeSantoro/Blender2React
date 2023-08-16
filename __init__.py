import bpy

# Globals
from . B2REACT_Globals import B2REACT_Globals

# Panels UI
from . B2REACT_UI import B2REACT_PT_Init_Panel
# from . B2REACT_UI import B2REACT_PT_Edit_Panel
from . B2REACT_UI import B2REACT_PT_Utils_Panel
from . B2REACT_UI import B2REACT_PT_Export_Panel
from . B2REACT_UI import B2REACT_PT_gltfjsx_Options
from . B2REACT_UI import B2REACT_PT_Transform_Options
from . B2REACT_UI import B2REACT_PT_ExportActions

# Initialization Operators
from . init.create_r3f_project import B2REACT_OT_Create_R3F_Project
from . init.reset_git import B2REACT_OT_Reset_Git
from . init.open_vscode import B2REACT_OT_Open_Project_in_VSCode
from . init.open_folder import B2REACT_OT_open_project_folder
from . init.start_dev_server import B2REACT_OT_StartDevServer
from . init.delete_r3f_project import B2REACT_OT_Delete_R3F_Project
from . init.re_inizialize import B2REACT_OT_Re_Initialize

from . init.update_title import B2REACT_OT_Update_Title

# Utilities
from . utils.pushdown_actions import B2REACT_OT_Push_Down_Actions
from . utils.rename_tracks import B2REACT_OT_RenameTracks
from .utils.rename_object import B2REACT_OT_RenameObject

# Export
# from . export.export_all_glb import R3F_OT_ExportAll_GLB
from . export.export_active_glb import B2REACT_OT_Export_Active_GLB


bl_info = {
    "name": "Blender 2 React",
    "author": "Robe Santoro",
    "description": "Bring a Blender project to React Three Fiber",
    "blender": (3, 6, 0),
    "version": (0, 0, 1),
    "location": "View3D > UI > Blender 2 React",
    "category": "Blender2React"
}


def register():

    # Register Globals
    bpy.utils.register_class(B2REACT_Globals)
    bpy.types.Scene.Blender2React = bpy.props.PointerProperty(type=B2REACT_Globals)

    # Register Panels UI
    bpy.utils.register_class(B2REACT_PT_Init_Panel)
    # bpy.utils.register_class(B2REACT_PT_Edit_Panel)
    bpy.utils.register_class(B2REACT_PT_Utils_Panel)
    bpy.utils.register_class(B2REACT_PT_Export_Panel)
    bpy.utils.register_class(B2REACT_PT_gltfjsx_Options)
    bpy.utils.register_class(B2REACT_PT_Transform_Options)
    bpy.utils.register_class(B2REACT_PT_ExportActions)
    

    # Register Init Operators
    bpy.utils.register_class(B2REACT_OT_Create_R3F_Project)
    bpy.utils.register_class(B2REACT_OT_Reset_Git)
    bpy.utils.register_class(B2REACT_OT_Open_Project_in_VSCode)
    bpy.utils.register_class(B2REACT_OT_open_project_folder)
    bpy.utils.register_class(B2REACT_OT_StartDevServer)
    bpy.utils.register_class(B2REACT_OT_Delete_R3F_Project)
    bpy.utils.register_class(B2REACT_OT_Re_Initialize)

    bpy.utils.register_class(B2REACT_OT_Update_Title)

    # Register Utilities
    bpy.utils.register_class(B2REACT_OT_Push_Down_Actions)
    bpy.utils.register_class(B2REACT_OT_RenameTracks)
    bpy.utils.register_class(B2REACT_OT_RenameObject)

    # bpy.utils.register_class(R3F_OT_ExportAll_GLB)
    bpy.utils.register_class(B2REACT_OT_Export_Active_GLB)


def unregister():

    # Unregister Panels UI
    bpy.utils.unregister_class(B2REACT_PT_Init_Panel)
    # bpy.utils.unregister_class(B2REACT_PT_Edit_Panel)
    bpy.utils.unregister_class(B2REACT_PT_Utils_Panel)
    bpy.utils.unregister_class(B2REACT_PT_Export_Panel)
    bpy.utils.unregister_class(B2REACT_PT_gltfjsx_Options)
    bpy.utils.unregister_class(B2REACT_PT_Transform_Options)
    bpy.utils.unregister_class(B2REACT_PT_ExportActions)

    # Unregister Init Operators
    bpy.utils.unregister_class(B2REACT_OT_Create_R3F_Project)
    bpy.utils.unregister_class(B2REACT_OT_Reset_Git)
    bpy.utils.unregister_class(B2REACT_OT_Open_Project_in_VSCode)
    bpy.utils.unregister_class(B2REACT_OT_open_project_folder)
    bpy.utils.unregister_class(B2REACT_OT_StartDevServer)
    bpy.utils.unregister_class(B2REACT_OT_Delete_R3F_Project)
    bpy.utils.unregister_class(B2REACT_OT_Re_Initialize)

    bpy.utils.unregister_class(B2REACT_OT_Update_Title)

    # Unregister Utilities
    bpy.utils.unregister_class(B2REACT_OT_Push_Down_Actions)
    bpy.utils.unregister_class(B2REACT_OT_RenameTracks)
    bpy.utils.unregister_class(B2REACT_OT_RenameObject)

    # bpy.utils.unregister_class(R3F_OT_ExportAll_GLB)
    bpy.utils.unregister_class(B2REACT_OT_Export_Active_GLB)

    # Unregister Globals
    bpy.utils.unregister_class(B2REACT_Globals)
    del bpy.types.Scene.Blender2React


if __name__ == "__main__":
    register()
