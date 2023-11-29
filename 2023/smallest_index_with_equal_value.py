"""
https://leetcode.com/problems/smallest-index-with-equal-value/
"""


class Solution:
    """
    Solution
    """

    def smallest_equal(self, nums: list[int]) -> int:
        """
        smallest_equal
        """
        for i, x in enumerate(nums):
            if i % 10 == x:
                return i

        return -1
