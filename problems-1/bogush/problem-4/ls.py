import argparse
import os


def ls(directory):
    names = os.listdir(directory)
    paths = (os.path.join(directory, name) for name in names)
    files = (path for path in paths if os.path.isfile(path))
    files = sorted(sorted(files), key=lambda file: os.stat(file).st_size)
    files = map(os.path.basename, files)
    return files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, default='.')
    a = parser.parse_args()
    if not os.path.isdir(a.dir):
        parser.print_help()
    print(*ls(a.dir), sep='\n')


if __name__ == "__main__":
    main()
