"""
https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/description/
"""


class Solution:
    """
    Solution
    """

    def find_column_width(self, grid: list[list[int]]) -> list[int]:
        """
        find column width
        """
        rslt: list[int] = []
        for col in zip(*grid):
            rslt.append(max(map(lambda item: len(str(item)), col)))

        return rslt
