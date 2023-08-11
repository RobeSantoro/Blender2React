import bpy


def export_glb(filepath, active_collection=True):

    # Export the GLB file
    bpy.ops.export_scene.gltf(
        filepath=filepath,
        export_format='GLB',
        export_copyright='RobeSantoro © 2023',
        will_save_settings=True,

        use_selection=False,
        use_visible=False,
        use_renderable=False,
        use_active_collection=active_collection,  # DOES NOT WORK ???
        use_active_collection_with_nested=True,
        use_active_scene=False,

        export_extras=True,
        export_cameras=False,
        export_lights=False,

        export_yup=True,

        export_apply=True,
        export_texcoords=True,
        export_normals=True,
        export_tangents=False,
        export_colors=False,
        use_mesh_edges=False,
        use_mesh_vertices=False,

        export_materials='EXPORT',
        export_image_format='AUTO',
        export_jpeg_quality=70,

        export_original_specular=False,

        export_morph=True,
        export_morph_normal=True,
        export_morph_tangent=False,

        export_rest_position_armature=True,
        export_def_bones=False,
        export_hierarchy_flatten_bones=False,

        export_skins=True,
        export_all_influences=False,

        export_import_convert_lighting_mode='SPEC',

        export_draco_mesh_compression_enable=False,  # NO DRACO ???

        export_animations=True,
        export_animation_mode='ACTIONS',
        export_bake_animation=False,

        export_current_frame=True,
        export_frame_range=True, 
        export_anim_slide_to_zero=False,
        export_negative_frame='SLIDE',
    
        export_anim_single_armature=True, 
        export_reset_pose_bones=True,  # Reset pose bones between actions

        export_morph_animation=True,
        export_morph_reset_sk_data=True,

        export_force_sampling=True,
        export_frame_step=1,

        export_optimize_animation_size=True,
        export_optimize_animation_keep_anim_armature=True,
        export_optimize_animation_keep_anim_object=False,
    )

    return
