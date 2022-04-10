"""
https://leetcode.com/problems/smallest-string-with-swaps/
"""


from collections import defaultdict


class DSU:
    def __init__(self, size: int) -> None:
        self.parents = list(range(size))

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px > py:
            px, py = py, px

        self.parents[py] = px


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        N = len(s)
        dsu = DSU(N)
        for x, y in pairs:
            dsu.union(x, y)

        # Collect all connected nodes.
        connectedNodes = defaultdict(list)
        for i, c in enumerate(s):
            connectedNodes[dsu.find(i)].append(c)

        # Sort the nodes in reverse order for each connected group.
        for key in connectedNodes.keys():
            connectedNodes[key].sort(reverse=True)

        # Compose the final minimum string.
        rslt = []
        for i in range(N):
            rslt.append(connectedNodes[dsu.find(i)].pop())

        return ''.join(rslt)
