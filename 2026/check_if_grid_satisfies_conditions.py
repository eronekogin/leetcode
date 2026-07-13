"""
https://leetcode.com/problems/check-if-grid-satisfies-conditions/description/
"""


class Solution:
    """
    Solution
    """

    def satisfies_conditions(self, grid: list[list[int]]) -> bool:
        """
        satisfies conditions
        """
        m, n = len(grid), len(grid[0])
        row = grid[-1]

        for c in range(0, n - 1):
            if row[c] == row[c + 1]:
                return False

        for c in range(n):
            for r in range(m - 2, -1, -1):
                if grid[r][c] != row[c]:
                    return False

        return True
