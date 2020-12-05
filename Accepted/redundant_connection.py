"""
https://leetcode.com/problems/redundant-connection/
"""


from typing import List


class DSU:

    def __init__(self, maxSize: int):
        self._parents = list(range(maxSize))
        self._ranks = [0] * maxSize

    def find(self, x: int) -> int:
        parent = self._parents[x]
        if parent != x:
            self._parents[x] = self.find(parent)

        return self._parents[x]

    def union(self, x: int, y: int) -> int:
        px, py = self.find(x), self.find(y)
        if px == py:  # Already unioned.
            return False

        rx, ry = self._ranks[px], self._ranks[py]
        if rx < ry:
            self._parents[px] = py
        elif rx > ry:
            self._parents[py] = px
        else:
            self._parents[py] = px
            self._ranks[px] += 1

        return True  # Union two nodes.


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(1001)  # Use disjoint set union structure.
        for edge in edges:
            if not dsu.union(*edge):
                return edge
