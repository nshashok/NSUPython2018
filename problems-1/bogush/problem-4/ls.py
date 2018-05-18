import argparse
import os
import sys


def ls(directory):
    names = os.listdir(directory)
    paths = (os.path.join(directory, name) for name in names)
    files = (path for path in paths if os.path.isfile(path))
    files_and_sizes = ((os.path.basename(file), os.stat(file).st_size) for file in files)
    return sorted(files_and_sizes, key=lambda fs: (-fs[1], fs[0]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, default='.')
    a = parser.parse_args()
    if not os.path.isdir(a.dir):
        print(a.dir, 'is not a directory', file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    try:
        for file, size in ls(a.dir):
            print(file, size, sep='\t')
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
