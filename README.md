# Keystroke Logger

This Python script continuously logs keystrokes to a file and runs in the background without appearing in the taskbar. It saves all recorded keystrokes to `keystrokes.txt` when the program exits. Additionally, it sets up auto-startup on system startup.

## Features

- Logs all keystrokes to `keystrokes.txt`.
- Runs in the background without appearing in the taskbar.
- Saves all recorded keystrokes when the program exits.
- Auto-starts on system startup.

## Installation

1. Clone or download this repository.

```bash
git clone https://github.com/your_username/keystroke-logger.git

Install the required Python libraries:
pip install pynput pystray
Replace "icon.png" with the path to your desired icon file.

Run the script:

bash
Copy code
python keystroke_logger.py
Auto-start on System Startup (Windows)
After running the script once, a shortcut named KeystrokeLogger.lnk will be created in the Windows startup folder.

The script will now run automatically on system startup.

Usage
The script continuously logs keystrokes to keystrokes.log.
To exit the program, right-click the system tray icon and select "Exit".
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

vbnet
Copy code

Replace `"your_username"` with your GitHub username in the installation instructions. This `README.md` provides clear instructions on how to install, run, and use the keystroke logger script, as well as how to set it up for auto-startup on Windows.


