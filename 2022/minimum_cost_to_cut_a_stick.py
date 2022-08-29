"""
https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
"""


from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        @lru_cache(None)
        def dp(start: int, end: int) -> int:
            if end - start <= 1:
                return 0

            return sortedCuts[end] - sortedCuts[start] + min(
                dp(start, mid) + dp(mid, end)
                for mid in range(start + 1, end)
            )

        sortedCuts = sorted(cuts + [0, n])
        return dp(0, len(sortedCuts) - 1)
