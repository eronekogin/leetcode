"""
https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def count_paths(self, grid: list[list[int]]) -> int:
        """
        count paths
        """
        @cache
        def dp(r: int, c: int):
            total = 0
            target = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > target:
                    total = (total + 1 + dp(nr, nc)) % mod

            return total

        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rslt = 0
        for r in range(m):
            for c in range(n):
                rslt = (rslt + dp(r, c)) % mod

        # Add m*n to the result for each single cell as a sequence
        return (rslt + m * n) % mod
