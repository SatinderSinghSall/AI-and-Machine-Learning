# File Handling in Python:

"""
---------------------------------------------------------
    PYTHON FILE HANDLING (BASIC → ADVANCED) – FULL CODE
---------------------------------------------------------
"""

import os
import shutil
import json
import csv


# -------------------------------------------------------
# 1. OPENING A FILE
# -------------------------------------------------------
# Syntax: open(filename, mode)
f = open("sample.txt", "w")   # creates/writes file
f.write("Hello, this is sample text.\n")
f.close()


# -------------------------------------------------------
# 2. READING A FILE
# -------------------------------------------------------
# read() – read full content
with open("sample.txt", "r") as f:
    print("READ():\n", f.read())

# readline() – read one line at a time
with open("sample.txt", "r") as f:
    print("READLINE():", f.readline())
    print("Next line:", f.readline())

# readlines() – returns list of lines
with open("sample.txt", "r") as f:
    print("READLINES():", f.readlines())


# -------------------------------------------------------
# 3. WRITING AND APPENDING DATA
# -------------------------------------------------------
# write() – overwrite content
with open("notes.txt", "w") as f:
    f.write("This is a new file created with write().")

# append() – add new content
with open("notes.txt", "a") as f:
    f.write("\nAppending new line using append mode.")


# -------------------------------------------------------
# 4. FILE EXISTENCE CHECK
# -------------------------------------------------------
print("File exists?" , os.path.exists("notes.txt"))


# -------------------------------------------------------
# 5. FILE DELETE & RENAME
# -------------------------------------------------------
if os.path.exists("temp.txt"):
    os.remove("temp.txt")  # delete only if exists

# create file to rename
open("old.txt", "w").close()
os.rename("old.txt", "renamed.txt")  # renaming


# -------------------------------------------------------
# 6. DIRECTORY (FOLDER) OPERATIONS
# -------------------------------------------------------
if not os.path.exists("NewFolder"):
    os.mkdir("NewFolder")            # create folder

os.makedirs("Nested/Folder/Path", exist_ok=True)  # nested folders

print("Directory list:", os.listdir())            # list items
os.chdir("NewFolder")                              # change directory
os.chdir("..")                                     # move back


# -------------------------------------------------------
# 7. COPY / MOVE / TREE OPERATIONS
# -------------------------------------------------------
with open("copy_source.txt", "w") as f:
    f.write("Copy this content.")

shutil.copy("copy_source.txt", "copied_file.txt")     # copy file
shutil.move("copied_file.txt", "moved_file.txt")      # move file
shutil.copytree("Nested", "Nested_Copy", dirs_exist_ok=True)


# -------------------------------------------------------
# 8. FILE METADATA
# -------------------------------------------------------
print("File Size:", os.path.getsize("sample.txt"), "bytes")
print("Absolute Path:", os.path.abspath("sample.txt"))


# -------------------------------------------------------
# 9. BINARY FILE HANDLING (image, mp3, pdf...)
# -------------------------------------------------------
with open("binary_sample.bin", "wb") as f:
    f.write(b'01010101 binary values')

with open("binary_sample.bin", "rb") as f:
    print("Binary Read:", f.read())


# -------------------------------------------------------
# 10. JSON FILE HANDLING
# -------------------------------------------------------
data = {
    "name": "Satinder",
    "skills": ["Python", "React", "MERN"]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # write JSON

with open("data.json", "r") as f:
    print("JSON Read:", json.load(f))


# -------------------------------------------------------
# 11. CSV FILE HANDLING
# -------------------------------------------------------
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Amit", 92])
    writer.writerow(["Tara", 88])

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV:", row)


# -------------------------------------------------------
# 12. FILE POINTER OPERATIONS  (tell, seek)
# -------------------------------------------------------
with open("sample.txt", "r") as f:
    print("\nPOINTER at:", f.tell())
    print("Read first 5 chars:", f.read(5))
    print("POINTER now:", f.tell())

    f.seek(0)   # move pointer to start
    print("After SEEK →\n", f.read())


# -------------------------------------------------------
# 13. EXCEPTION HANDLING IN FILES
# -------------------------------------------------------
try:
    with open("unknown.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\n⚠ Error: File not found!")


# -------------------------------------------------------
# END OF FILE HANDLING MASTER CODE
# -------------------------------------------------------
