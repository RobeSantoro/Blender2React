import bpy


class B2REACT_OT_Push_Down_Actions(bpy.types.Operator):
    """Push down actions of all selected objects"""

    bl_idname = "blender2react.push_down_actions"
    bl_label = "Push Down Actions"

    bl_description = "Push down actions of all selected objects"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    def execute(self, context):
        active_obj = context.active_object
        selected_objs = context.selected_objects

        if active_obj is None:
            self.report({'ERROR'}, "No active object")
            return {'CANCELLED'}

        for ob in selected_objs:
            # print(ob)
            if ob.animation_data is not None:
                action = ob.animation_data.action
                if action is not None:
                    track = ob.animation_data.nla_tracks.new()

                    # print(action.frame_range)
                    anim_start = round(action.frame_range[0], 0)

                    track.strips.new(action.name, int(anim_start), action)
                    ob.animation_data.action = None

        return {'FINISHED'}
