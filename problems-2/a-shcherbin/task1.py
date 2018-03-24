def inputNumber():

    print("Введите число:")

    while(True):
        try:
            line = input()
            int(line)
            return
        except EOFError:
            print("Ну и ладно")
            return
        except ValueError:
            print("Это не число")

if __name__ == '__main__':
    inputNumber()