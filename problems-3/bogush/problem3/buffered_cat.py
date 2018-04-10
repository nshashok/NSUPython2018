#!/usr/local/bin/python3
from sys import argv
from argparse import ArgumentParser
from file_buffer import file_buffer


def chars(fp):
    buffer = file_buffer(fp)
    if 'b' in fp.mode:
        for byte in buffer:
            yield byte
    else:
        for char in buffer:
            yield char


def buffered_cat(fp):
    for char in chars(fp):
        print(char, end='')


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('file', help='file to read')
    arg_parser.add_argument('-b', '--binary', dest='mode', action='store_const', const='rb', default='r',
                            help='if set then open file as binary, otherwise as text')
    args = arg_parser.parse_args(argv[1:])
    try:
        with open(args.file, args.mode) as fp:
            buffered_cat(fp)
    except Exception as e:
        print(e)
        exit(1)
    exit(0)


if __name__ == "__main__":
    main()

