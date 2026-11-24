import os
import shutil

from pathlib import Path

found_files = []

types = {
    Path("Videos"): (".mp4", ".mkv"),
    Path("Music"): (".mp3", ".wav"),
    Path("Pictures"): (".png", ".jpg", ".jpeg")
}

#Creating the folders at every start

def create_folders():
    for folder in types:
        #Check if folders exists, if not create.
        try:
            folder.mkdir()
            print(f"{folder} created.")
        except FileExistsError:
            print(f"{folder} already exists.")
        except FileNotFoundError:
            print("The parent directory does not exists.")
        except PermissionError:
            print("Permission denied")

# Move files (Not done Yet)
def move_files():

    if not found_files:
        print(f"No Files Found ❌")
        return
    
    input("Files Found. Press ENTER to continue")

    for file in found_files:
        for key, value in types.items():
            if file.lower().endswith(value):
                try:
                    shutil.move(file, key)
                    print(f"{file} -> {key} ✅")
                except shutil.Error as error:
                    print(f"{file} -> {key} ❌ -> {error}")


# Find Files and push in the array.
def find():

    for root, dirs, files in os.walk('.'):
        for name in files:
            for key, value in types.items():
                if name.lower().endswith(value):
                    found_files.append(name)
        break

def main():
    find()
    create_folders()
    move_files()

if __name__ == "__main__":
    main()