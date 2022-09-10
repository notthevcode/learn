import os
from datetime import datetime

os.chdir("/Users/notth/Desktop/")
# # Changes the directory, make sure it's a forward slashes and don't include drives letter and last slash is an optional slash
print(os.getcwd())
# print(os.getcwd())  # Gets the current working directory(Directory means it's a folder system which contains files which are used to refer other computer folders, files, in simple words it's a folder where the running file is at)
os.mkdir("testing10")
# Can't create multiple levels of directories here
os.makedirs("concepts-10/os-module")
# Creates folders, becareful though everytime you run, it creates the folders and throw an error of file existing error.
os.rmdir("testing10")
# Deletes the directory
os.removedirs("concepts-10/os-module")
# Deletes the directories
os.rename("learn", "Learn")
# Renaming the file
print(os.stat("bot"))
# Gives all the stats about a directory or file
print(os.stat("bot").st_size)
# Use Attributes method to know more details in more human readble form
mod_time = os.stat("bot").st_mtime
# This returns timestamp number and to convert into human readble form you need to use datetime module
print(datetime.fromtimestamp(mod_time))
# Here fromtmestamp method is used in datetime module
print(os.listdir())
# List all the directories in the current working directory or folder.

# ___________________________________________________________________________________________________________________________________________________________________________
# os.walk() method, if you forgot where is the file located this method helps greatly.

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()  # This gives nice space for every loop, so it's important to put it here and more cleaner way is written below as comment
    # print(
    #     f"Current Path: {dirpath}\nDirectories: {dirnames}\nFiles: {filenames}")
# ___________________________________________________________________________________________________________________________________________________________________________
# Environment variables

print(os.environ)
# Lists all the environment variables in the my computer
print(os.environ.get("HOMEPATH"))
# Returns my environment variable or users home Directory

"test.txt"
# Creating a file and now putting this file in the home directory is done by os.path.join() method and not string concatenation because it messes up slashes

file_path = os.path.join(os.environ.get("HOMEPATH"), "test.txt")
print(file_path)
# Now it's in the correct path

# Other Methods in the os.path
print(os.path.basename(file_path))
# Prints the file name: test.txt
print(os.path.dirname(file_path))
# Prints all the directories other than basename
print(os.path.split(file_path))
# Prints the directories and files in the list and you can access them with list indexes

print(os.path.exists("/Users/notth/conman-game.py"))
# Checks if the paths exists or not and returns booleans values: True or False

# Very Important
print(os.path.splitext(file_path))
# Returns the path without file extension, don't use slicing and shit method, this is easy and reliable

print(dir(os.path))
