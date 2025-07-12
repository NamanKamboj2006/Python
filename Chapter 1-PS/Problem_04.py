# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.
import os

directory_path = 'F:\Python\Chapter 1-PS'

try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
