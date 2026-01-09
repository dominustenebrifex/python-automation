import os

# Organizes files in the current directory by file type
# Excludes Python scripts to avoid breaking automation

files = os.listdir()

for file in files:
    if os.path.isfile(file):
        if file.endswith(".py"):
            continue  # Skip Python files

        if "." not in file:
            continue  # Skip files without extension

        ext = file.split(".")[-1]

        if not os.path.exists(ext):
            os.mkdir(ext)

        os.rename(file, f"{ext}/{file}")

print("Files organized successfully.")
