def answerlist(n):
    result = []
    power = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            power += 1
            n //= d
        else:
            if power > 0:
                m_list = [d, power]
                result.append(m_list)
            d += 1
            power = 0
    if n > 1:
        m_list = [n, power+1]
        result.append(m_list)
    return result


n = int(input("Enter a number: "))
print(answerlist(n))
