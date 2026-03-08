"""
https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/
"""


class Solution:
    """
    Solution
    """

    def largest_perimeter(self, nums: list[int]) -> int:
        """
        largest perimeter
        """
        total = sum(nums)
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            if total - nums[i] > nums[i]:
                return total

            total -= nums[i]

        return -1
