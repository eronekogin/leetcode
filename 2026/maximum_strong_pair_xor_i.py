"""
https://leetcode.com/problems/maximum-strong-pair-xor-i/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def maximum_strong_pair_xor(self, nums: list[int]) -> int:
        """
        Docstring for maximum_strong_pair_xor

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :return: Description
        :rtype: int
        """
        return max(
            x ^ y
            for x in nums
            for y in nums
            if abs(x - y) <= min(x, y)
        )
