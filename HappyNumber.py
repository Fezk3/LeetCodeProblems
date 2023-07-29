def isHappy(n: int) -> bool:

    visit = set() # set

    while n not in visit:
        visit.add(n)
        n = sumOfSquares(n)

        if n == 1:
            return True

    return False

def sumOfSquares(n: int) -> int:
    # compute the number digits
    res = 0

    while n:
        digit = n % 10  # last digit of the number
        digit = digit ** 2  # square it
        res += digit
        n = n // 10  # get next digit

    return res
