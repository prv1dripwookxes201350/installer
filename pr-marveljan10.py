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
import os

def delete_aesmarvel_conf():
    file_path = r"C:\Windows\System32\aesmarvel_conf.txt"
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied: Unable to delete '{file_path}'. Run the script as administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")
delete_aesmarvel_conf()

os.system('cls')
def stop_service():
    service_name = "vgk"
    try:
        # Run the command to stop the service
        result = subprocess.run(["net", "stop", service_name], capture_output=True, text=True, shell=True)

        # Output the result of the command
        if result.returncode == 0:
            print(f"Service '{service_name}' stopped successfully.")
        else:
            print(f"Failed to stop the service '{service_name}'.\nError: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")
stop_service()
os.system('cls')


import time
def check_timezone():
    local_time = time.localtime()
    utc_time = time.gmtime()
    time_difference = (time.mktime(local_time) - time.mktime(utc_time)) / 3600
    if time_difference != 8:
        send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "wrong time, not utc8+")
        os.system('cls')
        print("Set your timezone to UTC8+.")
        input()
        sys.exit()
check_timezone()


os.system('cls')
dcnmwxdr = r'C:\Windows\System32\DRVX'

if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')


import zipfile
import os


url = "https://raw.githubusercontent.com/elaidacruzsdfsdklxkou/installer/refs/heads/main/uniqueid_3.0.txt"
search_string = file_contentsx1
result = check_string_in_url(url, search_string)
print(result)
os.system('cls')

os.system('cls')
print("")
print("")
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\DRVX\aesmarv.py"
    files_to_delete = [
        r"C:\Windows\System32\DRVX\aespremium_nogui.py",
        r"C:\Windows\System32\DRVX\aespremium_nogui.bat",
        r"C:\Windows\System32\DRVX\pyarmor_runtime_000000"
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
                    print("Aes Software is updating, please don't close the window.")
                    print("Change log:")
                    print("---Improve security.")
                    print("")
                    print("")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\DRVX\\pyarmor_runtime_000000"):
    print("downloading required libraries, please wait a moment...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1aZWSUF1clTzPPLLZv9dcDfZ-Oi8E_dUD", "C:\\Windows\\System32\\DRVX\\aesmarv.zip")
    zip_file = r'C:\Windows\System32\DRVX\aesmarv.zip'
    extract_dir = r'C:\Windows\System32\DRVX'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


import os
import shutil
os.system('cls')

def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")


required_version = (3, 11, 5)
current_version = sys.version_info[:3]

if current_version != required_version:
    os.system('cls')
    print(f"Failed version.")
    input()
    os.system('cls')
    sys.exit()
    exit()
else:
    print("Success.")

os.system('cls')
print("")
print("")
print("")
print("///For your safety, Valorant's anticheat has been completely disabled.")
print("///Press enter to continue...")
input()
def create_batch_file(python_command, script_name):
    directory = r"C:\Windows\System32\DRVX"
    filename = "aesmarv.bat"
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        batch_content = f"@echo off\n{python_command} {script_name} || echo errorwithpath"
        os.makedirs(directory, exist_ok=True)
        with open(filepath, 'w') as file:
            file.write(batch_content)
        print(f"")
    else:
        print("")
create_batch_file("py -3.11", r"C:\Windows\System32\DRVX\aesmarv.py")
batch_file_path = r"C:\Windows\System32\DRVX\aesmarv.bat"
os.system('cls')


try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")



os.system('cls')

os._exit(0)
sys.exit()
