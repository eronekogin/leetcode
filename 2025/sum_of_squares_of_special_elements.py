"""
https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
"""


class Solution:
    """
    Solution
    """

    def sum_of_squares(self, nums: list[int]) -> int:
        """
        sum of squares
        """
        return sum(
            x * x
            for i, x in enumerate(nums)
            if len(nums) % (i + 1) == 0
        )
