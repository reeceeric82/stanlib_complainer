# Stanlib Complainer:
I wrote this because despite my best efforts to get in contact with Stanlib. 
I had not heard from them for months and tried other avenues by myself to no avail. 
Even having issues such as being unable to login to my account so I made this. 

## How can I use it?
First install python:


 - [Windows_64](https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe)
 - [MacOSX](https://www.python.org/ftp/python/3.11.8/python-3.11.8-macos11.pkg)


Download a webdriver for your browser of choice:

- [Chrome](https://chromedriver.chromium.org/downloads)
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads)
- [Firefox](https://github.com/mozilla/geckodriver/releases)

Download this repo either as a zip file or `git clone`

Extract the repo and the webdriver, place the webdriver in the root of the project(where the main.py, requirements and so is).
In your terminal locate the project folder and enter it:

- Windows: `cd Desktop/stanlib_complainer/`
- MacOS: `cd Desktop/stablib_complainer/`

Enable the virtual enviroment:

- Windows: `python -m venv venv`
- MacOSX: `python -m venv venv`

Activate the enviroment:

- Windows CMD: `venv\Scripts\activate.bat`
- Windows Powershell: `venv\Scripts\Activate.ps1`
- MacOS: `source myvenv/bin/activate`

Install the requirements:
 - Windows / MacOs: `pip install -r requirements.txt`

Open the main.py in an editor: Notepad, VsCode, Pycharm etc.
And change the values that are provided in CAPITALS

### Run It:

- `python main.py`

### Stop It:

- Press `Ctrl + C`