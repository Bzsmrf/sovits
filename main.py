import os
import subprocess
import zipfile
import urllib.request

REPO_URL = "https://github.com/Bzsmrf/so-vits-svc-fork.git"

# Branch (for development)
if not os.path.exists('so-vits-svc-fork'):
    os.system(f'git clone {REPO_URL}')
if not os.path.exists('input'):
    os.mkdir('input')
if not os.path.exists('output'):
    os.mkdir('output')

# download models
# MODELS = {
#     'drake': 'https://mega.nz/file/Sm53wAwI#4PmIrSWDrEP1-pnZb5MJpTcfoHy3OBhBOhn2FVxfyb8',
#     'kanye': 'https://mega.nz/file/Dr40kCQI#G3bEWPvUvTa9SBJKQt7rETgcFds4ssnJF0nGN9aAXTk',
#     'eminem': 'https://drive.google.com/file/d/1KVUMEEX4aTR5S-l1Chv4SO63SyoKKcv8/view'
# }

# for model_name, model_url in MODELS.items():
#     print(f'Downloading {model_name}...')
#     urllib.request.urlretrieve(model_url, f'{model_name}.zip')  
#     with zipfile.ZipFile(f'{model_name}.zip',"r") as zip_ref:
#         zip_ref.extractall("so-vits-svc-fork\src\so_vits_svc_fork\inference")


os.chdir('so-vits-svc-fork\src\so_vits_svc_fork\inference')

subprocess.run(['pip', 'install', 'so_vits_svc_fork'])

subprocess.run(['python', 'inference.py'])
