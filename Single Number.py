def singleNumber(nums: list[int]) -> int:
    res = []
    for num in nums:
        if num in res:
            res.remove(num)
        else:
            res.append(num)
    return res[0]


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2,1]))
