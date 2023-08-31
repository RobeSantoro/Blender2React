import bpy
import mathutils


class B2REACT_OT_ParentToEmpty(bpy.types.Operator):
    """ Parent the selected objects to an empty"""

    bl_idname = "blender2react.parent_to_empty"
    bl_label = "Parent to Empty"

    bl_description = "Parent the selected objects to an empty"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    def execute(self, context):

        selected_objects = context.selected_objects

        if not selected_objects:
            self.report({'WARNING'}, "No objects selected.")
            return {'CANCELLED'}

        # Get the center of the bounding box of the selected objects
        center = sum((obj.matrix_world.translation for obj in selected_objects),
                     mathutils.Vector()) / len(selected_objects)

        # Create an empty at the center of the bounding box
        bpy.ops.object.empty_add(location=center)

        for obj in selected_objects:
            empty = context.view_layer.objects.active

            # Select the object and then the empty
            obj.select_set(True)
            empty.select_set(True)
            context.view_layer.objects.active = empty

            # Parent the object to the empty
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

            # Rename the empty to the object name
            empty.name = obj.name + "_Empty"

            # Deselect the object and the empty
            obj.select_set(False)
            empty.select_set(False)

        return {'FINISHED'}
