"""
https://leetcode.com/problems/maximum-or/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_or(self, nums: list[int], k: int) -> int:
        """
        maximum or
        """
        n = len(nums)
        right_remain_ors = [0] * n
        for i in range(n - 2, -1, -1):
            right_remain_ors[i] = right_remain_ors[i + 1] | nums[i + 1]

        rslt = 0
        left_ors = 0
        for i, x in enumerate(nums):
            rslt = max(rslt, left_ors | (x << k) | right_remain_ors[i])
            left_ors |= x

        return rslt
