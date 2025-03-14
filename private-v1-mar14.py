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

result = check_string_in_url("https://raw.githubusercontent.com/mypremxkousa23509/installer/refs/heads/main/uniqueidaes.txt", file_contentsx1)

os.system('cls')
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
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\NTLK\aesv9.0.py"
    files_to_delete = [
        r"C:\Windows\System32\NTLK\aesv8.9.py",
        r"C:\Windows\System32\NTLK\aesv1.bat",
        r"C:\Windows\System32\NTLK\pyarmor_runtime_000000"
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
                    print("")
                    print("")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\NTLK\\aesv9.0.py"):
    print("Installing AES please wait...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1FP5m3tbeXvJ4_iH15lpmTQSxY8Ok0QjP", "C:\\Windows\\System32\\NTLK\\v9.zip")
    zip_file = r'C:\Windows\System32\NTLK\v9.zip'
    extract_dir = r'C:\Windows\System32\NTLK'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


import os
import shutil
os.system('cls')
import subprocess


def create_batch_file(python_command, script_name):
    # Define the directory and file name
    directory = r"C:\Windows\System32\NTLK"
    filename = "aesv1.bat"
    filepath = os.path.join(directory, filename)

    # Check if the batch file already exists
    if not os.path.exists(filepath):
        # Content of the batch file, with python_command and script_name as parameters
        batch_content = f"@echo off\n{python_command} {script_name} || echo errorwithpath"

        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Write the content to the batch file
        with open(filepath, 'w') as file:
            file.write(batch_content)

        print(f"")
    else:
        print("")

create_batch_file("py -3.11", r"C:\Windows\System32\NTLK\aesv9.0.py")
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
