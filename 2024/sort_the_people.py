"""
https://leetcode.com/problems/sort-the-people/description/
"""


class Solution:
    """
    Solution
    """

    def sort_people(self, names: list[str], heights: list[int]) -> list[str]:
        """
        sort people
        """
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
