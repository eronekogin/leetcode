"""
https://leetcode.com/problems/number-of-great-partitions/description/
"""


class Solution:
    """
    Solution
    """

    def count_partitions(self, nums: list[int], k: int) -> int:
        """
        count partitions
        """
        # Not enough numbers to be divided.
        if sum(nums) < (k << 1):
            return 0

        # Find the number of subset in nums having its sum less than k.
        dp = [1] + [0] * (k - 1)
        for x in nums:
            for i in range(k - 1 - x, -1, -1):
                dp[i + x] += dp[i]

        # The number in nums are either in group 1 or group 2, so the
        # total number of subsets are 2 ** n, and the total invalid
        # subset is sum(dp), and the invalid subset can either be in
        # group 1 or 2, so rslt = 2 ** n - sum(dp) * 2
        return ((1 << len(nums)) - (sum(dp) << 1)) % (10 ** 9 + 7)
