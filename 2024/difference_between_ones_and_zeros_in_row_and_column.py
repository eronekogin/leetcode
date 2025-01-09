"""
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
"""


class Solution:
    """
    Solution
    """

    def ones_minus_zeros(self, grid: list[list[int]]) -> list[list[int]]:
        """
        ones minus zeros
        """
        m, n = len(grid), len(grid[0])
        ones_cols = [0] * n
        ones_rows = [0] * m
        zero_cols = [0] * n
        zero_rows = [0] * m
        rslt = [[0] * n for _ in range(m)]

        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 0:
                    zero_cols[c] += 1
                    zero_rows[r] += 1
                else:
                    ones_cols[c] += 1
                    ones_rows[r] += 1

        for r in range(m):
            for c in range(n):
                rslt[r][c] = (
                    ones_rows[r] +
                    ones_cols[c] -
                    zero_cols[c] -
                    zero_rows[r]
                )

        return rslt
