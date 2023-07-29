class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}  # val : index

        for ind, num in enumerate(nums):
            dife = target - num
            if dife in dict:
                return [dict[dife], ind]
            dict[num] = ind
