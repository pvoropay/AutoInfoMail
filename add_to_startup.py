#!/usr/bin/env python 
import os
from win32com.client import Dispatch

def add_to_startup(file_path):
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    shortcut_path = os.path.join(startup_folder, "turn_on_email.lnk")
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = file_path
    shortcut.WorkingDirectory = os.path.dirname(file_path)
    shortcut.save()

if __name__ == "__main__":
    mail_script_path = r'~\TurnOn\mail.py' # change path to the mail.py script
    add_to_startup(mail_script_path)
