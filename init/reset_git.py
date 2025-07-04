import os
import shutil
import subprocess
import re
import bpy
import platform

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
        print('Deleting Actual Git Folder:', git_path)

        # If exists, delete .git folder
        if os.path.exists(git_path):
            shutil.rmtree(git_path, onerror=remove_readonly)
            print('.git Folder Deleted')
        else:
            print('Git Folder not found')

        # Always initialize git after deleting (or if not found)
        project_path = os.path.join(R3F_Project_Root, R3F_Project_Name)
        platform_system = platform.system()

        if platform_system == "Windows":
            # Windows command
            cmd = f'cd /d "{project_path}" && git init && git add . && git commit -m "New Initial Commit" && timeout 10 && exit'
            subprocess.Popen(["start", "cmd", "/k", cmd], shell=True)
            
        elif platform_system == "Darwin":
            # macOS command
            command = f"cd '{project_path}' && git init && git add . && git commit -m 'New Initial Commit' && sleep 10 && exit"
            apple_script = f'tell application "Terminal" to do script "{command}"'
            subprocess.Popen([
                "osascript",
                "-e",
                apple_script
            ])
        else:
            # Linux/Unix command
            command = f'cd "{project_path}" && git init && git add . && git commit -m "New Initial Commit" && sleep 10'
            subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", command])

        print('Executing git initialization in terminal...')
        print('Project path:', project_path)
        print("Git Initialized")
        print('-------------------------------------------------------')

        bpy.context.window_manager.popup_menu(
            lambda self, context:
                self.layout.label(text="Created a new git repo"),
                title="Git Reset Complete",
                icon='INFO')

        return {"FINISHED"}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)
