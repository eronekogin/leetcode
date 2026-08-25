"""
https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description/
"""


class Solution:
    """
    Solution
    """

    def calc(
        self, grid: list[list[int]], u: int, d: int, l: int, r: int
    ) -> int:
        min_i = len(grid)
        max_i = 0
        min_j = len(grid[0])
        max_j = 0

        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)

        return (
            (max_i - min_i + 1) * (max_j - min_j + 1)
            if min_i <= max_i
            else 901
        )

    def rotate(self, vec: list[list[int]]) -> list[list[int]]:
        n = len(vec)
        m = len(vec[0]) if n > 0 else 0
        ret = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                ret[m - j - 1][i] = vec[i][j]

        return ret

    def solve(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        res = n * m

        for i in range(n - 1):
            for j in range(m - 1):
                res = min(
                    res,
                    self.calc(grid, 0, i, 0, m - 1)
                    + self.calc(grid, i + 1, n - 1, 0, j)
                    + self.calc(grid, i + 1, n - 1, j + 1, m - 1),
                )

                res = min(
                    res,
                    self.calc(grid, 0, i, 0, j)
                    + self.calc(grid, 0, i, j + 1, m - 1)
                    + self.calc(grid, i + 1, n - 1, 0, m - 1),
                )

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = min(
                    res,
                    self.calc(grid, 0, i, 0, m - 1)
                    + self.calc(grid, i + 1, j, 0, m - 1)
                    + self.calc(grid, j + 1, n - 1, 0, m - 1),
                )

        return res

    def minimum_sum(self, grid: list[list[int]]) -> int:
        rgrid = self.rotate(grid)
        return min(self.solve(grid), self.solve(rgrid))
