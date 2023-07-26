import os
import shutil
import subprocess
import re
import bpy

from . delete_r3f_project import remove_readonly
from .. B2REACT_Globals import get_project_root, get_project_name

class B2REACT_OT_Reset_Git(bpy.types.Operator):
    """ Creates a git repo in the current folder """

    bl_idname = "blender2react.reset_git"
    bl_label = "Reset Git"

    bl_description = "Creates a fresh git repo for the current project"
    bl_options = {"REGISTER"}
    bl_category = "Blender2React"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        R3F_Project_Root = get_project_root()
        R3F_Project_Name = get_project_name()

        git_path = os.path.join(R3F_Project_Root, R3F_Project_Name, ".git")

        print('-------------------------------------------------------')
        print('Deleting Template Git Folder:', git_path)

        # If exists
        if os.path.exists(git_path):

            # Delete .git folder
            shutil.rmtree(git_path, onerror=remove_readonly)
            print('.git Folder Deleted')
        
            cmd = f"cd {R3F_Project_Root + R3F_Project_Name}\
                && git init\
                && git add .\
                && git commit -m \"New\"\
                && timeout 15\
                && exit\
            "

            p = subprocess.Popen(["start", "cmd", "/k", f"{cmd}"], shell=True)
            p.wait()

            cmd_clean = re.sub(' {2,}', ' ', cmd)
            cmd_clean = cmd_clean.replace("&&", "&&\n")

            print('Executing command in path:', R3F_Project_Root + R3F_Project_Name, '\n')

            print("Git Initialized")
            print('-------------------------------------------------------')

        return {"FINISHED"}