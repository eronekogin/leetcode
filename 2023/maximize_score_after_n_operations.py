"""
https://leetcode.com/problems/maximize-score-after-n-operations/
"""


from math import gcd
from functools import cache


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        @cache
        def dp(mask: int, currStep: int):
            if mask == 0:  # no more numbers
                return 0

            rslt = 0
            for i in range(N - 1):
                if mask & (1 << i):
                    for j in range(i + 1, N):
                        if mask & (1 << j):
                            nextMask = mask & ~(1 << i) & ~(1 << j)
                            rslt = max(
                                rslt,
                                currStep * gcd(nums[i], nums[j]) +
                                dp(nextMask, currStep + 1)
                            )

            return rslt

        N = len(nums)
        return dp((1 << N) - 1, 1)


print(Solution().maxScore([3, 4, 6, 8]))
