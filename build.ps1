# Windows Powershell build script
.\venv\Scripts\activate
pyinstaller --hidden-import=openpyxl -F -w -y -n RosterCompare main.py