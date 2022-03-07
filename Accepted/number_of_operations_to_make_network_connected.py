"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""


class DSU:
    def __init__(self, size: int) -> None:
        self.parents = list(range(size))

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        self.parents[self.find(y)] = self.find(x)


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        # To make all nodes connected, at least n - 1 cables are needed.
        if len(connections) < n - 1:
            return -1

        dsu = DSU(n)
        for x, y in connections:
            dsu.union(x, y)

        return sum(i == p for i, p in enumerate(dsu.parents)) - 1


print(Solution().makeConnected(4,
                               [[0, 1], [0, 2], [1, 2]]))
