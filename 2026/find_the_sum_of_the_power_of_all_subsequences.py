"""
https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/description/
"""


class Solution:
    """
    Solution
    """

    def sum_of_power(self, nums: list[int], k: int) -> int:
        """
        sum of power
        """
        m = 10 ** 9 + 7

        dp = [1] + [0] * k
        for x in nums:
            for v in range(k, -1, -1):
                dp[v] = (
                    dp[v] +  # Not taking x
                    dp[v] +  # taking x
                    (dp[v - x] if v >= x else 0)
                ) % m

        return dp[k]
