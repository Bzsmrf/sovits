import os
import urllib
import subprocess

REPO_URL = "https://github.com/Bzsmrf/so-vits-svc-fork.git"


# Branch (for development)
if not os.path.exists('so-vits-svc-fork'):
    os.system(f'git clone {REPO_URL}')
if not os.path.exists('input'):
    os.mkdir('input')
if not os.path.exists('output'):
    os.mkdir('output')


os.chdir('so-vits-svc-fork\src\so_vits_svc_fork\inference')

subprocess.run(['pip', 'install', 'so_vits_svc_fork'])

subprocess.run(['python', 'inference.py'])
