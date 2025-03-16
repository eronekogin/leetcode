"""
https://leetcode.com/problems/minimum-cost-to-split-an-array/description/
"""


from collections import Counter
from functools import cache


class Solution:
    """
    Solution
    """

    def min_cost(self, nums: list[int], k: int) -> int:
        """
        min cost
        """
        @cache
        def dp(i: int) -> int:
            """
            dp[i] stands for the minimum cost starting
            from index i.
            """
            if i == len(nums):
                return 0

            min_cost = 10 ** 13
            memo = Counter()
            dup_cnt = 0

            for j in range(i, len(nums)):
                memo[nums[j]] += 1

                if memo[nums[j]] == 2:
                    dup_cnt += 2
                elif memo[nums[j]] > 2:
                    dup_cnt += 1

                importance = k + dup_cnt

                if importance >= min_cost:
                    break

                min_cost = min(
                    min_cost,
                    importance + dp(j + 1)
                )

            return min_cost

        return dp(0)
