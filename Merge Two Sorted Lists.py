def mergeTwoLists(list1, list2):
    l = []
    if len(list1) == 0:
        return list2
    else:
        num = len(list1)

    for n in range(num):
        l.append(list1[n])
        l.append(list2[n])

    return l

print(mergeTwoLists([1,2,4],[1,3,4]))