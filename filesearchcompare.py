import os
from collections import defaultdict

def get_file_map(path):
    """
    Returns a dictionary mapping filename -> list of full paths
    """
    file_map = defaultdict(list)
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            file_map[file].append(full_path)
    return file_map
def get_files_from_unc(path):

    fileuset = set()
    for root, _, files in os.walk(path):
        for file in files:
            fileuset.add(file)
    return fileuset

def find_duplicates(path1, path2):
    files1 = get_files_from_unc(path1)
    files2 = get_files_from_unc(path2)

    duplicates = files1.intersection(files2)

    return duplicates
def find_duplicate_paths(path1, path2):
    files1 = get_file_map(path1)
    files2 = get_file_map(path2)

    duplicates = {}
    for filename in files1.keys() & files2.keys():  # only filenames in both
        duplicates[filename] = {
            "path1": files1[filename],
            "path2": files2[filename]
        }
    return duplicates

if __name__ == "__main__":
    # Example UNC paths – replace with your actual ones
    unc_path1 = r"\\millervillenas\ebooks\Calibre Library"
    unc_path2 = r"\\millervillenas\ebooks\Adult"

    duplicates = find_duplicate_paths(unc_path1, unc_path2)

    if duplicates:
        print("Duplicate file names with full paths found:\n")
        for filename, paths in duplicates.items():
            print(f"File: {filename}")
            for p in paths["path1"]:
                print(f"  Path1: {p}")
            for p in paths["path2"]:
                print(f"  Path2: {p}")
            print("-" * 60)
    else:
        print("No duplicate file names found.")