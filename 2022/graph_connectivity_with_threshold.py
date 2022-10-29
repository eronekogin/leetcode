"""
https://leetcode.com/problems/graph-connectivity-with-threshold/
"""


class DSU:
    def __init__(self, size: int):
        self.parents = list(range(size))
        self.ranks = [0] * size

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        else:
            self.parents[px] = py
            self.ranks[py] += self.ranks[px] == self.ranks[py]


class Solution:
    def areConnected(
        self,
        n: int,
        threshold: int,
        queries: list[list[int]]
    ) -> list[bool]:
        dsu = DSU(n + 1)

        for x in range(threshold + 1, n):
            for y in range(x * 2, n + 1, x):
                # y is always multiples of x, and x, y shares a common factor
                # x that is greater than threshold.
                dsu.union(x, y)

        return [
            dsu.find(x) == dsu.find(y)
            for x, y in queries
        ]
