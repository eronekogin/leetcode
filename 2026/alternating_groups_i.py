"""
https://leetcode.com/problems/alternating-groups-i/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_alternating_groups(self, colors: list[int]) -> int:
        """
        number of alternating groups
        """
        colors += [colors[0], colors[1]]
        return sum(
            colors[i - 1] != colors[i] and colors[i] != colors[i + 1]
            for i in range(1, len(colors) - 1)
        )
