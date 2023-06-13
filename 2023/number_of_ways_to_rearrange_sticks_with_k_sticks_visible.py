"""
https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/
"""


from functools import cache


class Solution:
    @cache
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        Consider the last stick in the target arrangement:
        1. If it is the largest stick, then we have to pick k - 1 sticks from
            the remaining n - 1 sticks, which will be dp[n][k] += dp[n - 1][k - 1]

        2. Else, we have to pick k sticks from the remaining n - 1 sticks, and
            for the last stick, we have n - 1 choices, so it will be
            dp[n][k] += dp[n - 1][k] * (n - 1)
        """
        if n == k:
            return 1

        if k == 0:
            return 0

        return (
            self.rearrangeSticks(n - 1, k - 1) +
            self.rearrangeSticks(n - 1, k) * (n - 1)
        ) % (10 ** 9 + 7)
