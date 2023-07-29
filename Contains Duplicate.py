def duplicate(a):
    dic = {}
    cont = 0

    for n in a:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1

    for v in dic.values():
        if v < 2:
            cont += 1
    if cont != len(a):
        return False

    return True


print(duplicate([1,1,1,3,3,4,3,2,4,2]))