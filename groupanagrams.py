class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        for word in strs:
            key = tuple(sorted(word))
            dic[key] = dic.get(key, []) + [word]
        return dic.values()

# test it
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
