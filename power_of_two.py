def powe(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    while n > 1:
        n /= 2
    return n == 1

print(powe(3))
