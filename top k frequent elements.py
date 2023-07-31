class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        res = []

        for n in nums:
            if dic.get(n):
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1

        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(sorted_dic[i][0])

        return res


# test it
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))