"""
https://leetcode.com/problems/bricks-falling-when-hit/
"""


from typing import Iterator


class DSU:
    def __init__(self, R: int, C: int):
        N = R * C + 1
        self.N = N - 1
        self.parents = list(range(N))
        self.ranks = [0] * N
        self.size = [1] * N

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:  # Already unioned.
            return

        rx, ry = self.ranks[px], self.ranks[py]
        if rx < ry:
            rx, ry = ry, rx
        elif rx == ry:
            self.ranks[px] += 1

        self.parents[py] = px
        self.size[px] += self.size[py]

    def top(self) -> int:
        # Do not count the last node itself.
        return self.size[self.find(self.N)] - 1


class Solution:
    def hitBricks(
            self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        def index(r: int, c: int) -> int:
            return r * C + c

        def neighbors(r: int, c: int) -> Iterator[int]:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr, nc)

        R, C = len(grid), len(grid[0])

        # First initial the final bricks by hitting all the target bricks
        # on the grid.
        finalBricks = [list(row) for row in grid]
        for r, c in hits:
            finalBricks[r][c] = 0

        dsu = DSU(R, C)
        fakeNode = R * C  # A fake node where the top nodes will be unioned to.

        # Initialize dsu based on the finalBricks.
        for r, row in enumerate(finalBricks):
            for c, v in enumerate(row):
                if v:
                    i = index(r, c)
                    if r == 0:  # Top brick.
                        dsu.union(i, fakeNode)

                    if r and finalBricks[r - 1][c]:  # Above brick.
                        dsu.union(i, index(r - 1, c))

                    if c and finalBricks[r][c - 1]:  # Left brick.
                        dsu.union(i, index(r, c - 1))

        # Add each hit brick back to the grid and see how many new bricks will
        # be brought to the dsu.
        falledBricks = []
        for r, c in reversed(hits):
            preBricks = dsu.top()
            if not grid[r][c]:  # Hit on a blank cell.
                falledBricks.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if finalBricks[nr][nc]:
                        dsu.union(i, index(nr, nc))

                if r == 0:  # Top brick.
                    dsu.union(i, fakeNode)

                finalBricks[r][c] = 1
                falledBricks.append(max(0, dsu.top() - preBricks - 1))

        return falledBricks[::-1]


print(Solution().hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]))
