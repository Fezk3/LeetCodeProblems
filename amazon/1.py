from math import ceil

def findTotalExecutionTime(execution):
    dic = {}
    time = 0
    for index, num in enumerate(execution):
        if num not in dic:
            dic[num] = [index]
        else:
            dic[num].append(index)


    for num in execution:
        time += num
        if num in dic:
            for i in dic[num]:
                execution[i] = ceil(num / 2)

    return time

execution = [5,5,3,6,5,3]
print(findTotalExecutionTime(execution))
