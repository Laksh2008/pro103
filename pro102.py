import os
import shutil

from_dir = os.path.expanduser("~/Downloads")
to_dir = "/document_files"

list_of_files = os.listdir(from_dir)
print (list_of_files)

for file_name in list_of_files:
    # Get the file name and extension using os.path.splitext()
    name, ext = os.path.splitext(file_name)
    print(f"File name: {name}, Extension: {ext}")
    # List of valid extensions
valid_extensions = ['.txt', '.doc', '.docx', '.pdf']


    # If the extension is blank, continue to the next file
if not ext:
    continue

    # If the extension is valid, move the file to the corresponding directory
    if ext in valid_extensions:
        # Set the source, destination, and directory paths
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)

        # If the destination directory exists, move the file
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path2}")
            shutil.move(path1, path3)
        # If the destination directory doesn't exist, create it and then move the file
        else:
            os.makedirs(path2)
            print(f"Moving {file_name} to {path2}")
            shutil.move(path1, path3)