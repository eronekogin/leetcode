"""
https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_cost(self, nums: list[int]) -> int:
        """
        minimum cost
        """
        first, second = sorted(nums[1:3])
        for i in range(3, len(nums)):
            if nums[i] < first:
                first, second = nums[i], first
            elif nums[i] < second:
                second = nums[i]

        return nums[0] + first + second
