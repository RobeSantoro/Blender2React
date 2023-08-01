import bpy


class B2REACT_OT_RenameGeo(bpy.types.Operator):
    """Rename the geometry objects"""

    bl_idname = "blender2react.rename_geo"
    bl_label = "Rename Geometry"

    bl_description = "Rename the geometry objects"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    def execute(self, context):

        selected_objects = context.selected_objects

        for ob in selected_objects:
            if ob.type == 'MESH':
                ob.data.name = ob.name + "_geo"

        return {'FINISHED'}
