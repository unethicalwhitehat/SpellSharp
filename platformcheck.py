import platform

# Function to check the platform the program is running on

def PlatformCheck():
    if platform.system() == "Windows":
        return "Windows"
    elif platform.system() == "Mac":
        return "Mac"
    elif platform.system() == "Linux":
        return "Linux"
    else:
        return "Unknown"
