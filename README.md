Example install from source:
- First install python 3.6+
- Navigate to /mortgage-toolkit and enter pip install . in the same repo as setup.py


Example pyinstaller build executable:
pyinstaller --onefile --hidden-import=utils my_script.py

OR 

pyinstaller --onefile --add-data "utils.py:." my_script.py (LINUX/macOS)

OR 

pyinstaller --onefile --add-data "utils.py;." mortgage_toolkit_cli.py (WINDOWS)

- If running on windows you will see a .exe, in linux you will not.
- Note: utils.py must be added as a hidden import or additional data.
- If re-compiling with pyinstaller remove build and dist directories