#!/bin/bash
pyinstaller --argv-emulation --hidden-import=openpyxl -F -w -y -n RosterCompare main.py