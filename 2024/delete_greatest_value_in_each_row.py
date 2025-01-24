"""
https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
"""


class Solution:
    """
    Solution
    """

    def delete_greatest_value(self, grid: list[list[int]]) -> int:
        """
        delete greatest value
        """
        cnt = 0

        for row in grid:
            row.sort()

        for c in range(len(grid[0])):
            cnt += max(row[c] for row in grid)

        return cnt
