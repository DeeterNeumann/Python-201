# Add the code for the file counter script that you wrote in the course.

# Write a script that locates your Desktop
# Fetch all the files that are on there, and counts how many files of each different file type there are
# Use a dictionary to collect this data
# Print it to your console at the end in order to get an overview of what is there.
# Now expand file mover script
# Add logic that moves all file types that have, e.g., more than five files on the desktop into their own separate folder.
# Parse this string input and convert it back into a list of dictionaries that you can use to access information.

list = [{}, {}, {}]

#/Users/drneu
#/Users/drneu/OneDrive/Desktop

import pathlib
import pprint

file_counter = {}

drneu = pathlib.Path("/Users/drneu/OneDrive/Desktop")

# new_path = pathlib.Path("/Users/drneu/screenshots") ****CREATE FILE NAME BASED ON SUFFIX NAME??
# new_path.mkdir(exist_ok=True)


for filepath in drneu.iterdir():
    if filepath.suffix not in file_counter:
        file_counter[filepath.suffix] = []
    file_counter[filepath.suffix].append(filepath)

# print(file_counter)

for file_type, file_list in file_counter.items():
    if len(file_list) >= 5:
        new_folder_path = drneu.joinpath(file_type)
        new_folder_path.mkdir(exist_ok=True)
        for file in file_list:
            new_file_path = new_folder_path.joinpath(file.name)
            file.replace(new_file_path)
        print(f"{file_type} : {len(file_list)} meets critera")

# filed = open("files_counted.txt", "a")
# filed.write(str(file_counter))
# filed.write("\n")
# filed.close()
        
# filed = open("files_counted.txt", "r")
# contents = filed.read()
# filed.close()

# print(contents)
# print(type(contents))

# contents_split = contents.split()

# for ext in contents_split:
#     if ext == ".png":
#         egfe

