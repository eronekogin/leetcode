"""
https://leetcode.com/problems/find-the-value-of-the-partition/description/
"""


class Solution:
    """
    Solution
    """

    def find_value_of_partition(self, nums: list[int]) -> int:
        """
        find value of partition
        """
        nums.sort()
        return min(b - a for a, b in zip(nums, nums[1:]))
