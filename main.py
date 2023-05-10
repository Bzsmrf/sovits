import os
import subprocess
import urllib.request
from mega import Mega
import gdown
import zipfile

REPO_URL = "https://github.com/Bzsmrf/so-vits-svc-fork.git"

# Branch (for development)
if not os.path.exists('so-vits-svc-fork'):
    os.system(f'git clone {REPO_URL}')
if not os.path.exists('input'):
    os.mkdir('input')
if not os.path.exists('output'):
    os.mkdir('output')

# download models
mega = Mega()
m = mega.login()
m.download_url('https://mega.nz/file/Sm53wAwI#4PmIrSWDrEP1-pnZb5MJpTcfoHy3OBhBOhn2FVxfyb8')
m.download_url('https://mega.nz/file/Dr40kCQI#G3bEWPvUvTa9SBJKQt7rETgcFds4ssnJF0nGN9aAXTk')
# gdown.download('https://drive.google.com/uc?id=1KVUMEEX4aTR5S-l1Chv4SO63SyoKKcv8')

with zipfile.ZipFile("drake05.zip","r") as zip_ref:
    zip_ref.extractall("so-vits-svc-fork\src\so_vits_svc_fork\inference")
with zipfile.ZipFile("ye200k.zip","r") as zip_ref:
    zip_ref.extractall("so-vits-svc-fork\src\so_vits_svc_fork\inference")
# with zipfile.ZipFile("eminem general model 86k.zip","r") as zip_ref:
#     zip_ref.extractall("so-vits-svc-fork\src\so_vits_svc_fork\inference")


os.chdir('so-vits-svc-fork\src\so_vits_svc_fork\inference')

subprocess.run(['pip', 'install', 'so_vits_svc_fork'])

subprocess.run(['python', 'inference.py'])