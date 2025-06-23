"""
https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/
"""


class Solution:
    """
    Solution
    """

    def maximize_sum(self, nums: list[int], k: int) -> int:
        """
        maximize sum
        """
        max_num = max(nums)
        return ((max_num + (max_num + k - 1)) * k) >> 1
