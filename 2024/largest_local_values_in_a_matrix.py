"""
https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
"""


class Solution:
    """
    Solution
    """

    def largest_local(self, grid: list[list[int]]) -> list[list[int]]:
        """
        largest local
        """
        n = len(grid)
        max_grid = [[0] * (n - 2) for _ in range(n - 2)]
        for r in range(1, n - 1):
            for c in range(1, n - 1):
                max_grid[r - 1][c - 1] = max(
                    grid[r - 1][c - 1],
                    grid[r - 1][c],
                    grid[r - 1][c + 1],
                    grid[r][c - 1],
                    grid[r][c],
                    grid[r][c + 1],
                    grid[r + 1][c - 1],
                    grid[r + 1][c],
                    grid[r + 1][c + 1]
                )

        return max_grid
