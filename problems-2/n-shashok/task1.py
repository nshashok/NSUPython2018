import sys


def ask_input():
    inp = input("Input number: ")
    return int(inp)

if __name__ == "__main__":
    while True:
        try:
            num = ask_input()
            print("\tEntered:", num)
            break
        except EOFError:
            print("\tEOF")
            break
        except ValueError:
            print("\tInvalid", file=sys.stderr)
