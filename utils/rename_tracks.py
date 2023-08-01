import bpy


class B2REACT_OT_RenameTracks(bpy.types.Operator):
    """Rename Tracks in Active Collection"""

    bl_idname = "blender2react.rename_tracks"
    bl_label = "Rename Tracks"

    bl_description = "Rename Tracks in Active Collection"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    def execute(self, context):
        print("\nRenaming the tracks...")

        active_collection = bpy.context.view_layer.active_layer_collection.collection

        # Rename the NLA Tracks to the name of the collection name
        for ob in active_collection.all_objects:

            if ob.animation_data is not None and ob.animation_data.nla_tracks is not None:
                # print("ANIMATED:", ob.name, "\nCOLLECTION:", active_collection.name)
                for track in ob.animation_data.nla_tracks:

                    if ob.name.startswith("_"):
                        print("\nWARNING: Object name starts with _")
                        track.name = ob.name[1:]
                        print()

                    else:
                        track.name = active_collection.name

                    print("TRACK:", track.name, "OBJECT:", ob.name)

        print("Renaming done.\n")

        return {'FINISHED'}
