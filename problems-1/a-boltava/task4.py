import sys
import os

def get_files_list(path: str):
    files = []

    for entry_name in os.listdir(path):
        entry_path = os.path.join(path, entry_name)
        if os.path.isfile(entry_path):
            file_size = os.stat(entry_path).st_size
            files.append((entry_name, file_size))

    files.sort(key=lambda entry: (-entry[1], entry[0]))
    return files


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            for file_name, file_size in get_files_list(sys.argv[1]):
                print(file_name, file_size)
        except Exception as e:
            print(e)
    else:
        print("Usage: python {0} path".format(sys.argv[0]))
        print("path - path to scan for files")
