import bpy


class Blender2ReactPanel():

    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "blender2react"


class B2REACT_PT_Init_Panel(bpy.types.Panel, Blender2ReactPanel):
    """Blender2React Initialization Panel"""

    bl_idname = "B2REACT_PT_Init_Panel"
    bl_label = "Initialization"
    bl_description = "Initialization"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        row0 = layout.row(align=False)
        row0.prop(context.scene.Blender2React,
                  "R3F_Initialized", text="Initialized")
        row0.operator("Blender2React.re_initialize",
                      text="Re Init", icon='FILE_REFRESH')

        # NOT INITIALIZED - INIT
        if not bpy.context.scene.Blender2React.R3F_Initialized:
            col1 = layout.column(align=True, heading="Project_Root")
            col1.prop(context.scene.Blender2React, "R3F_Project_Root", text="")

            col2 = layout.column(align=True, heading="Project_Name")
            col2.prop(context.scene.Blender2React, "R3F_Project_Name", text="")

            row_init = layout.row(align=True)
            row_init.scale_y = 1.2 if context.scene.Blender2React.R3F_Initialized else 2
            row_init.operator("Blender2React.create_r3f_project",
                              text="Create R3F Project" if not context.scene.Blender2React.R3F_Initialized else "Project Created")
            row_init.enabled = not context.scene.Blender2React.R3F_Initialized

        # INITIALIZED - UPDATE TITLE
        else:
            col3 = layout.column(align=False)
            col3.label(text="Project_Title")

            row1 = layout.row(align=True)
            row1.prop(context.scene.Blender2React,
                      "R3F_Project_Title", text="")
            row1.operator("blender2react.update_title",
                          text="", icon='FILE_REFRESH')

        # START DEV SERVER OPERATOR
        row_dev = layout.row(align=False)
        row_dev.operator("Blender2React.start_dev_server")
        row_dev.scale_y = 1.5 if context.scene.Blender2React.R3F_Initialized else 1

        # OPEN IN VS CODE AND OPEN IN EXPLORER OPERATORS
        row_open = layout.row(align=False)
        row_open.operator("Blender2React.open_project_in_vscode")
        row_open.operator("Blender2React.open_project_folder")
        row_open.enabled = context.scene.Blender2React.R3F_Initialized

        # GIT INIT and # RESET OPERATOR
        row_reset = layout.row(align=False)
        row_reset.operator("Blender2React.reset_git")
        row_reset.enabled = context.scene.Blender2React.R3F_Initialized
        row_reset.operator("Blender2React.delete_r3f_project",
                           text="Delete Project")
        row_reset.enabled = context.scene.Blender2React.R3F_Initialized


class B2REACT_PT_Utils_Panel(bpy.types.Panel, Blender2ReactPanel):
    """Blender2React Utils Panel"""

    bl_idname = "B2REACT_PT_Utils_Panel"
    bl_label = "Utils"
    bl_description = "Blender2React Utils Panel"

    def draw(self, context):
        layout = self.layout

        col2 = layout.column(align=True)
        col2.operator("blender2react.rename_object",
                      text="Rename Object", icon='MESH_DATA')

        col2.separator()

        col1 = layout.column(align=True)
        col1.operator("blender2react.push_down_actions",
                      text="Push Down Selected", icon='ACTION')
        col1.operator("blender2react.rename_tracks",
                      text="Rename Tracks ", icon='ACTION_TWEAK')
        
        col1.separator()

        col1.operator("blender2react.parent_to_empty",
                        text="Parent to Empty", icon='EMPTY_DATA')


class B2REACT_PT_Export_Panel(bpy.types.Panel, Blender2ReactPanel):
    """Blender2React Export Panel"""

    bl_idname = "B2REACT_PT_Export_Panel"
    bl_label = "Export"
    bl_description = "Blender2React Export Panel"

    def draw(self, context):
        layout = self.layout

        col3 = layout.column(align=True, heading="R3F_Export_Path")
        col3.prop(context.scene.Blender2React, "R3F_Export_Path", text="")


class B2REACT_PT_gltfjsx_Options(bpy.types.Panel, Blender2ReactPanel):

    bl_idname = "B2REACT_PT_gltfjsx_Options"
    bl_label = "gltfjsx Options"
    bl_parent_id = "B2REACT_PT_Export_Panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout

        col = layout.column(align=True)
        # col.prop(context.scene.Blender2React,
        #          "R3F_JSX_typescript", text="Add Typescript Types")
        col.prop(context.scene.Blender2React,
                 "R3F_JSX_keepnames", text="Keep Names")
        col.prop(context.scene.Blender2React,
                 "R3F_JSX_keepgroups", text="Keep Groups")
        col.prop(context.scene.Blender2React,
                 "R3F_JSX_shadows", text="Shadows")
        col.prop(context.scene.Blender2React,
                 "R3F_JSX_printwidth", text="Print Width")
        col.prop(context.scene.Blender2React,
                 "R3F_JSX_precision", text="Precision")
        col.prop(context.scene.Blender2React,
                 "R3F_JSX_debug", text="Debug")

        col.prop(context.scene.Blender2React,
                 "R3F_JSX_transform", text="Transform (Optimize)")


class B2REACT_PT_Transform_Options(bpy.types.Panel, Blender2ReactPanel):

    bl_idname = "B2REACT_PT_TransformOptions"
    bl_label = "Transform Options"
    bl_parent_id = "B2REACT_PT_gltfjsx_Options"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout
        box = layout.box()

        if bpy.context.scene.Blender2React.R3F_JSX_transform:
            box.enabled = True
        else:
            box.enabled = False

        box.prop(context.scene.Blender2React,
            "R3F_JSX_instance", text="Instance")

        box.prop(context.scene.Blender2React,
                 "R3F_JSX_resolution", text="Resolution")
        box.prop(context.scene.Blender2React,
                 "R3F_JSX_keepmeshes", text="Keep Meshes")
        box.prop(context.scene.Blender2React,
                 "R3F_JSX_keepmaterials", text="Keep Materials")
        box.prop(context.scene.Blender2React, "R3F_JSX_format", text="Format")


class B2REACT_PT_ExportActions(bpy.types.Panel, Blender2ReactPanel):

    bl_idname = "B2REACT_PT_ExportActions"
    bl_label = "Export Actions"
    bl_parent_id = "B2REACT_PT_Export_Panel"
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):

        layout = self.layout
        col1 = layout.column(align=True, heading="")
        col1.prop(context.scene.Blender2React,
                  "R3F_Delete_Original_GLB", text="Delete Original GLB")
        col1.prop(context.scene.Blender2React,
                  "R3F_Delete_JSX_Component", text="Delete JSX Component")

        row2 = layout.row(align=True)
        row2.scale_y = 2
        row2.operator("Blender2React.export_active_glb",
                      text=f"Export `{context.view_layer.active_layer_collection.name}` Collection")

        # row1 = layout.row(align=True)
        # row1.operator("Blender2React.exportall_glb", text="Export All Collections")
