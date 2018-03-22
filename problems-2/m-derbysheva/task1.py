def integer():
    while True:
        try:
            int(input("Please enter a number "))
            break
        except ValueError:
            print("This is not a number. "
                  "Please enter a number or exit with Ctrl + D")
        except EOFError:
            break


integer()
