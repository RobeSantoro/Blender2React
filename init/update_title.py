
import os
import re
import bpy

from .. B2REACT_Globals import get_project_title


class B2REACT_OT_Update_Title(bpy.types.Operator):
    """Update the R3F Project Title and the corresponding title tag in index.html"""

    bl_idname = "blender2react.update_title"
    bl_label = "Update the R3F Project Title"
    bl_description = "Update the R3F Project Title and the corresponding title tag in index.html"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        R3F_Project_Root = bpy.context.scene.Blender2React.R3F_Project_Root
        R3F_Project_Name = bpy.context.scene.Blender2React.R3F_Project_Name
        R3F_Project_Title = get_project_title()

        # Update Title tag in index.html
        project_location = os.path.join(R3F_Project_Root, R3F_Project_Name)
        index_path = os.path.join(project_location, 'index.html')

        with open(index_path, 'r') as f:
            html = f.read()

        pattern = r"<title>.*?</title>"
        match = re.search(pattern, html, re.DOTALL)

        if match:
            title_tag = match.group()

            with open(index_path, 'w') as f:
                f.write(html.replace(
                    title_tag,
                    f"<title>{R3F_Project_Title}</title>")
                )

            print()
            print(f"Title tag in index.html")
            print(title_tag)
            print(f'updated to: {R3F_Project_Title}')
            print()

        return {"FINISHED"}
