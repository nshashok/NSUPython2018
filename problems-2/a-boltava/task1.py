def parse_int_from_stdin():
    integer_parsed = False
    eof = False
    integer = None
    
    while not integer_parsed and not eof:
        try:
            print("Enter a base 10 integer: ", end='')
            integer = int(input())
            integer_parsed = True
        except EOFError:
            print()
            eof = True
        except Exception as e:
            print(str(e))

    return integer if integer_parsed else None


if __name__ == '__main__':
    integer = parse_int_from_stdin()
    if integer is not None:
        print("Got integer: " + str(integer))
    else:
        print("No integer entered")
