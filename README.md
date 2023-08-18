# PeopleSoft Roster Difference Checker
This application is designed to check for students that add
or drop between two different roster files from PeopleSoft

## Running the Application
You can either run the application using a pre-compiled binary from
the [Released Page](https://github.com/MStolen/peoplesoft-roster-diff/releases)
or by installing the required Python discrepancies as explained in the installation section and running
```python -m main``` from the installed virtual environment (activate the virtual environment in the command line by 
running ```source venv/bin/activate``` on MacOS/Linux and ```.\venv\Scripts\activate``` on Windows).

### Operation
The user will be presented with two file selection windows:
1. A window to select the older roster file
2. A window to select the newer roster file

The files should be in CSV, XLS, or XLSX format. **Due to some strange behavior by PeopleSoft, you may need to open the
files it exports and re-save them in the correct format**.

The program will then determine which students have added and dropped the course and prompt the user to select a save
location for the output file (in CSV format).

## Installation
To install the application, you need Python 3 installed.
Once Python 3 is installed, run one of the setup scripts using
```./setup.sh``` or ```.\setup.ps1```.

## Building The Application
Building the application is currently only supported in MacOS and 
Windows. You can run the build script for the OS (```./build.sh``` or ```.\build.ps1```).