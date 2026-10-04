"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/description/
"""


class Solution:
    """
    Solution
    """

    def min_flips(self, grid: list[list[int]]) -> int:
        """
        min flips
        """
        rslt = 0
        m, n = len(grid) >> 1, len(grid[0]) >> 1

        # Handle non-middle rows and cols
        for r in range(m):
            for c in range(n):
                v = (
                    grid[r][c] +
                    grid[r][~c] +
                    grid[~r][c] +
                    grid[~r][~c]
                )

                # Either make all 4 cells 1 or 0
                rslt += min(v, 4 - v)

        diff = 0
        ones = 0

        # Handle middle row and col
        if len(grid[0]) & 1:
            for r in range(m):
                diff += grid[r][n] ^ grid[~r][n]
                ones += grid[r][n] + grid[~r][n]

        if len(grid) & 1:
            for c in range(n):
                diff += grid[m][c] ^ grid[m][~c]
                ones += grid[m][c] + grid[m][~c]

        # Handle the center, it must be 0, otherwise
        # the total ones cannot be divisible by 4
        if len(grid[0]) & 1 and len(grid) & 1:
            rslt += grid[m][n]

        if diff == 0 and ones % 4 > 0:
            # when diff is zero, ones is an even number,
            # where ones % 4 can either be 0 or 2
            rslt += 2

        return rslt + diff
