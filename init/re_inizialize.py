import os
import bpy

from .. B2REACT_Globals import get_scene_path, get_project_root, get_project_name


class B2REACT_OT_Re_Initialize(bpy.types.Operator):
    """Re-Initialize Global Folder Properties based on the location of the current .blend file"""

    bl_idname = "blender2react.re_initialize"
    bl_label = "Re-Initialize"

    bl_description = "Re-Initialize Global Folder Properties based on the location of the current .blend file"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
             
        # Check if the Blender Scene has been saved
        Scene_Path = get_scene_path()
        if Scene_Path is None:
            self.report({"ERROR"}, "Please save the Blender Scene before creating a R3F Project")
            return {"CANCELLED"}

        # Set R3F Project Root from the actual Blender Scene Path
        R3F_Project_Root = bpy.path.abspath("//")
        bpy.context.scene.Blender2React.R3F_Project_Root = R3F_Project_Root

        # Check if the R3F Project Root contains a folder named as the R3F Project Name
        R3F_Project_Name = get_project_name()
        Project_Path = os.path.join(R3F_Project_Root, R3F_Project_Name)

        if (os.path.exists(Project_Path)):

            bpy.context.scene.Blender2React.R3F_Project_Name = R3F_Project_Name

            # Setting Initialized
            bpy.context.scene.Blender2React.R3F_Initialized = True

            # Setting Export Path
            bpy.context.scene.Blender2React.R3F_Export_Path = os.path.join(
                R3F_Project_Root, R3F_Project_Name, "public"
            )
        else:
            self.report({"ERROR"}, "R3F Project not found in the current Blender Scene Path")
            return {"CANCELLED"}

        return {"FINISHED"}