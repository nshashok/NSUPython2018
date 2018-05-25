#!/usr/bin/python3

def give_me_int_or_eof():
    while True:
        try:
            value = int(input(), 0)
            break
        except EOFError:
            break
        except ValueError:
            continue

give_me_int_or_eof()
