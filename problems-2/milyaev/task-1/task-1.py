def get_number_from_stdin():
    print("Enter the number:")

    while True:
        try:
            return int(input())
        except ValueError:
            print("Entered string is not a number. Try again")
        except EOFError:
            return None


if __name__ == '__main__':
    number = get_number_from_stdin()
    if number is not None:
        print("Got number:", number)
    else:
        print("Got EOF, number is not entered")
