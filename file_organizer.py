import os

# Organizes files in the current directory by file type

files = os.listdir()

for file in files:
    if os.path.isfile(file):
        ext = file.split('.')[-1]

        if not os.path.exists(ext):
            os.mkdir(ext)

        os.rename(file, f"{ext}/{file}")

print("Files organized successfully.")
