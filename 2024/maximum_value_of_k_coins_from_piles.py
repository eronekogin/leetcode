"""
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def max_value_of_coins(self, piles: list[list[int]], k: int) -> int:
        """
        max value of coins
        """
        @cache
        def dp(i: int, remain: int):
            """
            means the maximum total we can get by getting k coins from pile
            i to pile n - 1
            """
            if remain == 0 or i == len(piles):
                return 0

            rslt, curr = dp(i + 1, remain), 0
            for j in range(min(len(piles[i]), remain)):
                curr += piles[i][j]
                rslt = max(rslt, curr + dp(i + 1, remain - j - 1))

            return rslt

        return dp(0, k)
