def compareTriplets(a, b):
    l = [0, 0]
    for i in range(3):
        if a[i] == b[i]:
            pass
        elif a[i] > b[i]:
            l[0] += 1
        else:
            l[1] += 1
    return l


print(compareTriplets([5, 6, 7], [3, 6, 10]))
print(compareTriplets([17, 28, 30], [99, 16, 8]))