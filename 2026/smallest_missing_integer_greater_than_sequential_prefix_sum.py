"""
https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/
"""


class Solution:
    """
    Solution
    """

    def missing_integer(self, nums: list[int]) -> int:
        """
        missing integer
        """
        i = 0
        n = len(nums)
        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1

        curr_sum = (nums[0] + nums[i]) * (i + 1) // 2

        while curr_sum in set(nums):
            curr_sum += 1

        return curr_sum
