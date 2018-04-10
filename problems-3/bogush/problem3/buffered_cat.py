#!/usr/local/bin/python3
from sys import argv
from argparse import ArgumentParser
from typing import IO


def chars(fp: IO, buff_size: int=5):
    while True:
        read_bytes = fp.read(buff_size)
        if len(read_bytes) == 0:
            return
        if 'b' not in fp.mode:
            read_bytes = read_bytes.encode()
        for byte in read_bytes:
            yield chr(byte)


def process(fp):
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
            process(fp)
    except Exception as e:
        print(e)
        exit(1)
    exit(0)


if __name__ == "__main__":
    main()

