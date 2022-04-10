"""
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x - 1
        while l + 1 < r:
            m = (l + r) // 2
            if m * m < x:
                l = m
            elif m * m > x:
                r = m
            else:
                return m

        return l


print(Solution().mySqrt(2))
