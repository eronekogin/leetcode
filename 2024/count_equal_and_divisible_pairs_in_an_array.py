"""
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def count_pairs(self, nums: list[int], k: int) -> int:
        """
        count pairs
        """
        return sum(
            (i * j) % k == 0
            for i in range(len(nums) - 1)
            for j in range(i + 1, len(nums))
            if nums[i] == nums[j]
        )
