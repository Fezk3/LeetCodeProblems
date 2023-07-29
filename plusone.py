def plusOne(digits: list[int]) -> list[int]:

    num = ''
    sol = []

    for n in digits:
        n = str(n)
        num = num + n

    res = int(num) + 1

    for n in str(res):
        sol.append(n)

    return sol

print(plusOne([1,2,3,4]))
print(plusOne([1,2,3,9]))
print(plusOne([9]))