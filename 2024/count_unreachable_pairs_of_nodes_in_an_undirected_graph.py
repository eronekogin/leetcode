"""
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
"""


from collections import Counter


class DSU:
    """
    Disjoint Set Union
    """

    def __init__(self, size: int) -> None:
        self.parents: list[int] = list(range(size))

    def find(self, x: int):
        """
        find parent
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int):
        """
        union two nodes
        """
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parents[px] = py


class Solution:
    """
    Solution
    """

    def count_pairs(self, n: int, edges: list[list[int]]) -> int:
        """
        count pairs
        """
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)

        total = 0
        for x in Counter(dsu.find(i) for i in range(n)).values():
            total += x * (n - x)

        return total >> 1


print(Solution().count_pairs(11, [[5, 0], [1, 0], [10, 7], [
      9, 8], [7, 2], [1, 3], [0, 2], [8, 5], [4, 6], [4, 2]]))
