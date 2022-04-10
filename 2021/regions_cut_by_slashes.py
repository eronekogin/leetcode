"""
https://leetcode.com/problems/regions-cut-by-slashes/
"""


class DSU:
    def __init__(self):
        self.p = {}

    def find(self, x: int) -> int:
        self.p.setdefault(x, x)
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x: int, y: int) -> None:
        self.p[self.find(x)] = self.find(y)

    def count(self) -> int:
        return len(set(map(self.find, self.p)))


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        """
        1. Suppose each grid is split by its diagonals and each triangle is
            marked as follows:

           -----------
           | \  0 /  |
           |  \  /   |
           | 3 \/ 1  |
           |   / \   |
           |  / 2 \  |
           | /     \ |
           -----------

        2. Then each (r - 1).2 is connected to r.0, each (c - 1).1 is connected
            to c.3

        3. When v is / or blank, 0 is connected to 3, 1 is connected to 2.
        4. When v is \ or blank, 0 is connected to 1, 3 is connected to 2.

        Then we could use disjoint union set to union those nodes and then
        count how many set in the final result. 
        """
        dsu = DSU()
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if r:  # Connect (r - 1).2 with r.0
                    dsu.union((r - 1, c, 2), (r, c, 0))

                if c:  # Connect (c - 1).1 with c.3
                    dsu.union((r, c - 1, 1), (r, c, 3))

                if v != '\\':
                    dsu.union((r, c, 3), (r, c, 0))
                    dsu.union((r, c, 2), (r, c, 1))

                if v != '/':
                    dsu.union((r, c, 1), (r, c, 0))
                    dsu.union((r, c, 2), (r, c, 3))

        return dsu.count()
