# Function to check if the program has been run before

def CheckIfFirstTimeRunning():
    try:
        f = open("ran", "r")
        f.close()
        return False
    except FileNotFoundError:
        f = open("ran", "w")
        f.close()
        return True