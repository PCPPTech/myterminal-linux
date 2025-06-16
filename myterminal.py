import os
from color_codes import *
installation_path = ""
try:
    with open(f"{os.path.expanduser('~')}/mtpaths.txt", "r") as f:
        installation_path = f.readlines[0] # the first line is the installation path
except FileNotFoundError:
    print(f"{red}[ERROR]{reset} file `mtpaths.txt` was not found.")
    print(f"{green}[NOTE]{reset} If you haven't yet, run `myterminal_install.py`.")
    print(f"{green}[NOTE]{reset} `myterminal_install.py` is the python script that creates the mtpaths.txt.")

print(installation_path)