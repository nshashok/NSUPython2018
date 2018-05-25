def integer():
    while True:
        try:
            val = int(input("Please enter a number "))
            print("your number is {0}".format(val))
            break
        except ValueError:
            print("This is not a number. "
                  "Please enter a number or exit with Ctrl + D")
        except EOFError:
            break


integer()
