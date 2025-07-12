import os

# Specify the directory you want to list (use '.' for current directory)
directory_path = 'F:\Python\Chapter 1-PS'

# List the contents of the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
