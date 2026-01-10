"""
https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/description/
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
        min_index = max_index = 0

        for i in range(index_difference, len(nums)):
            if nums[i - index_difference] > nums[max_index]:
                max_index = i - index_difference

            if nums[i - index_difference] < nums[min_index]:
                min_index = i - index_difference

            if nums[i] - nums[min_index] >= value_difference:
                return [min_index, i]

            if nums[max_index] - nums[i] >= value_difference:
                return [max_index, i]

        return [-1, -1]
