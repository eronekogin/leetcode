"""
https://leetcode.com/problems/right-triangles/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_right_triangles(self, grid: list[list[int]]) -> int:
        """
        number of right triangles
        """
        m, n = len(grid), len(grid[0])
        row_ones = [0] * m
        col_ones = [0] * n
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v:
                    row_ones[r] += 1
                    col_ones[c] += 1

        rslt = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v:
                    rslt += (row_ones[r] - 1) * (col_ones[c] - 1)

        return rslt


print(Solution().number_of_right_triangles(
    [[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
