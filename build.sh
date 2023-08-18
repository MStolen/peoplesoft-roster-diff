#!/bin/bash
# MacOS build script
INVENV=$(python -c 'import sys; print ("1" if hasattr(sys, "real_prefix") else "0")')
if [ "$INVENV" -eq "0" ]
then
    source venv/bin/activate
fi
pyinstaller --argv-emulation --hidden-import=openpyxl -F -w -y -n RosterCompare main.py