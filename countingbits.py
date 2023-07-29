class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        bit = 1
        for i in range(1, n+1):
            if bit * 2 == i:
                bit = i
            res[i] = 1 + res[i - bit]
        return res