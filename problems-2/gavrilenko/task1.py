

while True:
    try:
        number = int(input("Enter Your number: "))
        print("You made it")
        break
    except ValueError:
        print("It's not a number, try again.")
        continue
    except EOFError:
        print("EOF")
        break
