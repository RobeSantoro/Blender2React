import bpy


class B2R3F_PT_Init_Panel(bpy.types.Panel):
    """Blender2R3F Initialization Panel"""

    bl_idname = "B2R3F_PT_Init_Panel"
    bl_label = "Initialization"

    bl_description = "Initialization"
    bl_category = "Blender2R3F"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        col1 = layout.column(align=True, heading="R3F Project Root Location")
        col1.prop(context.scene.Blender2R3F, "R3F_Project_Root", text="", )

        col2 = layout.column(align=True, heading="R3F_Project_Name")
        col2.prop(context.scene.Blender2R3F, "R3F_Project_Name", text="")

        row1 = layout.row(align=True)
        row1.operator("Blender2R3F.create_r3f_project", text="Init")
        row1.operator("Blender2R3F.start_dev_server", text="Start Dev Server")

        row2 = layout.row(align=False)
        row2.operator("Blender2R3F.open_project_in_vscode", text="Open in VSCode")
        row2.operator("Blender2R3F.open_project_folder", text="Open in Explorer")


class B2R3F_PT_Utils_Panel(bpy.types.Panel):
    """Blender2R3F Utils Panel"""

    bl_idname = "B2R3F_PT_Utils_Panel"
    bl_label = "Utils"

    bl_description = "Blender2R3F Utils Panel"
    bl_category = "Blender2R3F"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        col1 = layout.column(align=True)
        # col1.label(text="Push Down Actions", icon='ACTION')
        col1.operator("Blender2R3F.pushdown_actions", text="Push Down Selected", icon='ACTION')

        col2 = layout.column(align=True)
        # col1.label(text="Push Down Actions", icon='ACTION')
        col2.operator("Blender2R3F.rename_tracks", text="Rename Tracks ", icon='ACTION_TWEAK')

        col3 = layout.column(align=True)
        # col1.label(text="Rename Geometry", icon='MESH_DATA')
        col3.operator("Blender2R3F.rename_geo", text="Rename Geometry", icon='MESH_DATA')


class B2R3F_PT_Export_Panel(bpy.types.Panel):
    """Blender2R3F Export Panel"""

    bl_idname = "B2R3F_PT_Export_Panel"
    bl_label = "Export"

    bl_description = "Blender2R3F Export Panel"
    bl_category = "Blender2R3F"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        col3 = layout.column(align=True, heading="R3F_Export_Path")
        col3.prop(context.scene.Blender2R3F, "R3F_Export_Path", text="")

        col1 = layout.column(align=True, heading="")
        col1.prop(context.scene.Blender2R3F, "R3F_Keep_Original_GLB", text="Keep Original GLB")
        col1.prop(context.scene.Blender2R3F, "R3F_Create_JSX_Component", text="Create JSX Component")

        row1 = layout.row(align=True)
        row1.operator("Blender2R3F.exportall_glb", text="Export All Collections")

        row2 = layout.row(align=True)
        row2.operator("Blender2R3F.exportselected_glb", text="Export Active Collection")
