# Importing module to check platform and os module to clear screen

import platformcheck
import os

# Function to clear the screen depending on the platform, as os.system('clear') doesn't work on Windows

def ClearScreen():
    if platformcheck.PlatformCheck() == "Windows":
        os.system('cls')
    else:
        os.system('clear')