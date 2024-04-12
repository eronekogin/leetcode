"""
https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def minimum_white_tiles(self, floor: str, num_carpets: int, carpet_len: int) -> int:
        """
        dp[i][k] stands for the minimum white tiles remain when covering the first
        i tiles with k carpets
        """
        @cache
        def dp(i: int, k: int):
            if i <= 0:
                return 0

            skip = dp(i - 1, k) + int(floor[i - 1])
            cover = dp(i - carpet_len, k - 1) if k > 0 else 1000
            return min(skip, cover)

        return dp(len(floor), num_carpets)
