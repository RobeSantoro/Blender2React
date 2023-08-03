import bpy


class B2REACT_OT_RenameObject(bpy.types.Operator):
    """Rename the geometry objects"""

    bl_idname = "blender2react.rename_object"
    bl_label = "Rename Geometry"

    bl_description = "Rename the geometry objects"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    def execute(self, context):

        selected_objects = context.selected_objects

        for ob in selected_objects:

            # Meshes
            if ob.type == 'MESH':
                ob.data.name = ob.name + "_geo"

            
            # Curves
            if ob.type == 'CURVE':
                ob.data.name = ob.name + "_curve"

            # Texts
            if ob.type == 'FONT':
                ob.data.name = ob.name + "_text"

        return {'FINISHED'}
