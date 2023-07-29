class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, num in enumerate(hash):
            if target - num in hash:
                return [hash[target - num], i]
            hash[num] = i