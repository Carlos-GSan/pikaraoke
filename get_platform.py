import os
import sys

def is_raspberry_pi():
    try: 
        return os.uname()[4][:3] == "arm"
    except AttributeError:
        return False

def get_platform():
    if is_raspberry_pi():
        return "raspberry_pi"
    elif sys.platform == "darwin":
        return "osx"
    elif sys.platform.startswith("linux"):
        return "linux"
    elif sys.platform.startswith("win"):
        return "windows"
    else:
        return "unknown"