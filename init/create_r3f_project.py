import os
import platform
import re
import subprocess
import bpy

from .. B2REACT_Globals import get_scene_path, get_project_root, get_project_name


def create_r3f_project(R3F_Project_Root="R3F_Project_Root",
                       R3F_Project_Name="R3F_Project_Name",
                       ):
    """Creates a R3F Project in a folder called as R3F_Project_Name in the given Root path"""

    os.chdir(R3F_Project_Root)

    cmd = f"\
        cd {R3F_Project_Root}\
        && git clone https://github.com/RobeSantoro/blender2react-template {R3F_Project_Name}\
        && cd {R3F_Project_Name}\
        && git remote rm origin\
        && npm install\
        && timeout 15\
        && exit\
        "

    # Clean cmd for printing
    cmd_clean = re.sub(' {2,}', ' ', cmd)
    cmd_clean = cmd_clean.replace("&&", "&&\n")
    print(cmd_clean)

    # Run cmd in a new terminal
    platform_system = platform.system()
    print('-------------------------------------------------------')
    print('----------------Creating R3F Project...----------------')
    print('-------------------------------------------------------')
    print()
    print('R3F_Project_Root:', R3F_Project_Root)
    print('R3F_Project_Name:', R3F_Project_Name)
    print()
    print("platform_system:", platform_system)

    if platform_system == "Windows":
        p = subprocess.Popen(["start", "cmd", "/k", f"{cmd}"], shell=True)
        p.wait()
    elif platform_system == "Darwin":
        try:
            output = os.system(cmd)
            print("output:", output)
            print(f" Project Created in {R3F_Project_Root}/{R3F_Project_Name}")
        except Exception as e:
            print(e)
    elif platform_system == "Linux":
        pass

    return


class B2REACT_OT_Create_R3F_Project(bpy.types.Operator):
    """Creates a R3F Project in a folder next to the current blender file if no path is given"""

    bl_idname = "blender2react.create_r3f_project"
    bl_label = "Create R3F Project"

    bl_description = "Creates a R3F Project  next to the current blender file"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        # Check if the Blender Scene has been saved
        Scene_Path = get_scene_path()
        if Scene_Path is None:
            self.report(
                {"ERROR"}, "Please save the Blender Scene before creating a R3F Project")
            return {"CANCELLED"}

        # Get R3F Project Root and Name from the UI
        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()

        # If Blender relative path is "//", set it to the absolute path
        if R3F_Project_Root.startswith("//"):
            R3F_Project_Root = bpy.path.abspath(R3F_Project_Root)
            bpy.context.scene.Blender2React.R3F_Project_Root = R3F_Project_Root

        # Create R3F Project
        create_r3f_project(R3F_Project_Root, R3F_Project_Name)

        # Setting Initialized
        bpy.context.scene.Blender2React.R3F_Initialized = True

        # Setting Export Path
        bpy.context.scene.Blender2React.R3F_Export_Path = os.path.join(
            R3F_Project_Root, R3F_Project_Name, "public"
        )

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        row = self.layout
        row.prop(context.scene.Blender2React,
                 "R3F_Project_Root", text="Project Root")
        row.prop(context.scene.Blender2React,
                 "R3F_Project_Name", text="Project Name")
        row.label(
            text="If no path is given, will create a 'r3f-project' folder next to the blender file")
