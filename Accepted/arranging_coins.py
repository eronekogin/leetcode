"""
https://leetcode.com/problems/arranging-coins/
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = l + ((r - l) >> 1)
            staircases = (m * (m + 1)) >> 1
            if staircases > n:
                r = m - 1
            elif staircases == n:
                return m
            else:
                l = m + 1

        return r


print(Solution().arrangeCoins(8))
