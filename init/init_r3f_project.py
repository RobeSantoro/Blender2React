import os
import re
import subprocess
import bpy

# from .. B2DREI_Globals import get_scene_path, get_project_root, get_project_name


class B2DREI_OT_Init_R3F_Project(bpy.types.Operator):
    """Creates a R3F Project in a folder next to the current blender file if no path is given"""

    bl_idname = "Blender2R3F.create_r3f_project"
    bl_label = "Create R3F Project"

    bl_description = "Creates a R3F Project in a folder next to the current blender file"
    bl_options = {"REGISTER"}
    bl_category = "Blender2R3F"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        Scene_Path = get_scene_path()

        if Scene_Path is None:
            return {"CANCELLED"}

        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()

        if R3F_Project_Root is None:
            print("No R3F Project Path given")
            self.report({"ERROR"}, "No R3F Project Path given")
            return {"CANCELLED"}

        print('_______________________________________________________')
        print("Scene_Path:", Scene_Path)
        print("R3F_Project_Root:", R3F_Project_Root)
        print("R3F_Project_name:", R3F_Project_Name)
        print("Creating Vite R3F Project...")

        # Check if the path exists and if not create it and change to it
        if not os.path.exists(R3F_Project_Root):
            os.mkdir(R3F_Project_Root)
        os.chdir(R3F_Project_Root)

        cmd = f"cd {R3F_Project_Root}\
            && npm create vite@latest {R3F_Project_Name} -- --template react\
            && cd {R3F_Project_Name}\
            && npm install three @react-three/fiber @react-three/drei @react-three/postprocessing r3f-perf\
            && git init\
            && git add .\
            && git commit -m \"Initial\"\
            && timeout 15\
            && exit\
        "

        p = subprocess.Popen(["start", "cmd", "/k", f"{cmd}"], shell=True)
        p.wait()

        cmd_clean = re.sub(' {2,}', ' ', cmd)

        print("cmd:", cmd_clean)
        print('-------------------------------------------------------')

        # Setting Export Path
        bpy.context.scene.Blender2R3F.R3F_Export_Path = R3F_Project_Root + "\\" + R3F_Project_Name + "\\public\\"

        return {"FINISHED"}
