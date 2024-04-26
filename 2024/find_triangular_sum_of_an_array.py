"""
https://leetcode.com/problems/find-triangular-sum-of-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def triangular_sum(self, nums: list[int]) -> int:
        """
        triangular_sum
        """
        curr_nums = nums
        while len(curr_nums) > 1:
            curr_nums = [
                (x + y) %
                10 for x, y in zip(curr_nums, curr_nums[1:])
            ]

        return curr_nums.pop()
