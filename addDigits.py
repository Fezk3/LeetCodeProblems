def addDigits(num: int) -> int:
    res
    while res > 9:
        num = str(num)
        for n in num:
            n = int(n)
            res = res + n

    return res

print(addDigits(38))