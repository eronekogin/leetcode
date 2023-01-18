"""
https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
"""


from collections import Counter, defaultdict


class DSU:
    def __init__(self, size: int):
        self.parents = list(range(size))

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        self.parents[px] = py


class Solution:
    def minimumHammingDistance(
        self,
        source: list[int],
        target: list[int],
        allowedSwaps: list[list[int]]
    ) -> int:
        N = len(source)
        dsu = DSU(N)
        for x, y in allowedSwaps:
            dsu.union(x, y)

        memo = defaultdict(set)
        for i in range(N):
            memo[dsu.find(i)].add(i)

        diffs = 0
        for members in memo.values():
            cntSource = Counter(source[i] for i in members)
            cntTarget = Counter(target[i] for i in members)
            diffs += sum((cntSource - cntTarget).values())

        return diffs
