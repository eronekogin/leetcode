"""
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_max_or_subsets(self, nums: list[int]) -> int:
        """
        count_max_or_subsets
        """
        dp = Counter([0])
        for x in nums:
            for k, v in list(dp.items()):
                dp[k | x] += v

        return dp[max(dp)]
