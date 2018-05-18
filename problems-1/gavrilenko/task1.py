

def getList(n):
    array = []
    number = 2

    while n > 1:
        count = 0

        while n % number == 0:
            n //= number
            count += 1
        if count != 0:
            array += [[number, count]]
        number += 1
    return array

