
# Automation Script for Renaming Files
import os

# Define directory
directory = './files_to_rename/'

# Rename files
for count, filename in enumerate(os.listdir(directory)):
    new_name = f"renamed_file_{count}.txt"
    src = os.path.join(directory, filename)
    dst = os.path.join(directory, new_name)
    os.rename(src, dst)
    print(f"Renamed {filename} to {new_name}")
