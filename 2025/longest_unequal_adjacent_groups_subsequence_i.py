"""
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def get_longest_subsequence(self, words: list[str], groups: list[int]) -> list[str]:
        """
        Docstring for get_longest_subsequence

        :param self: Description
        :param words: Description
        :type words: list[str]
        :param groups: Description
        :type groups: list[int]
        :return: Description
        :rtype: list[str]
        """
        rslt: list[str] = []
        prev = 1 - groups[0]
        for i, x in enumerate(groups):
            if x != prev:
                prev = x
                rslt.append(words[i])

        return rslt
