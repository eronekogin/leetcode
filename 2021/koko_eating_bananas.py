"""
https://leetcode.com/problems/koko-eating-bananas/
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def is_possible(speed: int) -> bool:
            """
            Determine whether koko could finish each pile of bananas within
            the target hours. Notice that for each pile, the hour cost is
            Math.ceil(p / speed), which is (p - 1) // speed + 1.
            """
            return sum((p - 1) // speed + 1 for p in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            m = l + ((r - l) >> 1)
            if is_possible(m):
                r = m
            else:
                l = m + 1

        return l
