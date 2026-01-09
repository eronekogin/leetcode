"""
https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_indices(self, nums: list[int], index_difference: int, value_difference: int) -> list[int]:
        """
        Docstring for find_indices

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :param index_difference: Description
        :type index_difference: int
        :param value_difference: Description
        :type value_difference: int
        :return: Description
        :rtype: list[int]
        """
        n = len(nums)
        for start in range(n - index_difference):
            for end in range(start + index_difference, n):
                if abs(nums[end] - nums[start]) >= value_difference:
                    return [start, end]

        return [-1, -1]
