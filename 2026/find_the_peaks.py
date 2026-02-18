"""
https://leetcode.com/problems/find-the-peaks/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_peaks(self, mountain: list[int]) -> list[int]:
        """
        Docstring for find_peaks

        :param self: Description
        :param mountain: Description
        :type mountain: list[int]
        :return: Description
        :rtype: list[int]
        """
        return [
            i
            for i in range(1, len(mountain) - 1)
            if mountain[i - 1] < mountain[i] > mountain[i + 1]
        ]
