def uniqueOccurrences(arr: list[int]) -> bool:

    dict = {}
    res = []

    for n in arr:
        n = str(n)
        dict[n] = 0

    for n in arr:
        n = str(n)
        if n in dict:
            dict[n] = dict[n] + 1

    for v in dict.values():
        if v in res:
            return False
        else:
            res.append(v)

    return True


print(uniqueOccurrences([1,2,3,2,3,3,1]))