"""
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
"""


class DSU:
    def __init__(self, size: int):
        self.parents = list(range(size))
        self.ranks = [1] * size

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        if self.ranks[px] > self.ranks[py]:
            px, py = py, px

        self.parents[px] = py
        self.ranks[py] += self.ranks[px]


class Solution:
    def distanceLimitedPathsExist(
        self,
        n: int,
        edgeList: list[list[int]],
        queries: list[list[int]]
    ) -> list[bool]:
        sortedQueries = sorted(
            (w, u, v, i)
            for i, (u, v, w) in enumerate(queries)
        )
        sortedEdges = sorted(
            (w, u, v)
            for u, v, w in edgeList
        )

        dsu = DSU(n)
        rslt = [None] * len(queries)
        j = 0
        for w, u1, v1, i in sortedQueries:
            # Union the nodes that having its edge distance less than the
            # current limit, then check if the in the end the target nodes
            # u1 and v1 are connected.
            while j < len(sortedEdges) and sortedEdges[j][0] < w:
                _, u, v = sortedEdges[j]
                dsu.union(u, v)
                j += 1

            rslt[i] = dsu.find(u1) == dsu.find(v1)

        return rslt
