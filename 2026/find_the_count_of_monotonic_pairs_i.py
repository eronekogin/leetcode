"""
https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/description/
"""


class Solution:
    """
    Solution
    """

    def count_of_pairs(self, nums: list[int]) -> int:
        """
        count of pairs
        """
        mod = 10 ** 9 + 7
        n = len(nums)
        m = max(nums) + 1

        # dp[j] stands for the number of ways where arr1[i - 1] = j
        dp = [1] * m
        dp2 = [0] * m

        for i in range(1, n):
            d = max(nums[i] - nums[i - 1], 0)

            for j in range(d, nums[i] + 1):
                dp2[j] = (dp2[j - 1] + dp[j - d]) % mod

            dp, dp2 = dp2, [0] * m

        return sum(dp) % mod
