"""
https://leetcode.com/problems/design-neighbor-sum-service/description/
"""


class NeighborSum:
    """
    Neighbor Sum
    """

    def __init__(self, grid: list[list[int]]):
        n = len(grid)
        memo = [[0, 0] for _ in range(n * n)]
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                memo[v] = [r, c]

        self.memo = memo
        self.grid = grid

    def adjacent_sum(self, value: int) -> int:
        """
        adjancent sum
        """
        r, c = self.memo[value]
        n = len(self.grid)
        rslt = 0
        if r - 1 >= 0:
            rslt += self.grid[r - 1][c]

        if r + 1 < n:
            rslt += self.grid[r + 1][c]

        if c - 1 >= 0:
            rslt += self.grid[r][c - 1]

        if c + 1 < n:
            rslt += self.grid[r][c + 1]

        return rslt

    def diagonal_sum(self, value: int) -> int:
        """
        diagonal sum
        """
        r, c = self.memo[value]
        n = len(self.grid)
        rslt = 0

        if r - 1 >= 0 and c - 1 >= 0:
            rslt += self.grid[r - 1][c - 1]

        if r + 1 < n and c - 1 >= 0:
            rslt += self.grid[r + 1][c - 1]

        if r - 1 >= 0 and c + 1 < n:
            rslt += self.grid[r - 1][c + 1]

        if r + 1 < n and c + 1 < n:
            rslt += self.grid[r + 1][c + 1]

        return rslt
