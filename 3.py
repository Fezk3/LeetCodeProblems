def rec(a, b):
    if b == 0:
        return 1
    temp = rec(a, int(b / 2))
    if b % 2 == 0:
        return temp * temp
    else:
        return temp * temp * a

print(rec(2, 3))
print(rec(3, 5))

