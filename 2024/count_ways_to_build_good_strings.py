"""
https://leetcode.com/problems/count-ways-to-build-good-strings/description/
"""


class Solution:
    """
    Solution
    """

    def count_good_strings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        count good strings
        """
        dp = [1] + [0] * high  # number of good strings with length i.
        m = 10 ** 9 + 7

        for end in range(1, high + 1):
            if end >= zero:  # Append zero number of '0's
                dp[end] += dp[end - zero]

            if end >= one:  # Append one number of '1's
                dp[end] += dp[end - one]

            dp[end] %= m

        return sum(dp[low: high + 1]) % m
