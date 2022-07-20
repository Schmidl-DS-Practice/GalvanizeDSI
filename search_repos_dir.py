import os
from glob import glob

PATH = "~/Documents/SchoolDocs/Schmidl-DS-Practice/GalvanizeDSI/repos"

# this counter how many repos had .git in them
# print(sum(1 for _, dirnames, _ in os.walk("repos") if ".git" in dirnames))

# this worked to remove the .git directory from this dir
for dirpath, dirnames, _ in os.walk("repos"):
    if ".git" in dirnames:
        print(dirpath, dirnames)
        os.system(f"rm -rf {dirpath}/.git")


# this checked to ensure each .git was removed
i = 1
for dirpath, dirnames, _ in os.walk("repos"):
    if ".git" in dirnames:
        print(dirpath, dirnames, i)
        i += 1
    else:
        print("No more .git directories", i)