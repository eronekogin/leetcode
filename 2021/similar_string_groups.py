"""
https://leetcode.com/problems/similar-string-groups/
"""


from itertools import combinations
from collections import defaultdict


class DSU:

    def __init__(self, size: int):
        self.parents = list(range(size))

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        self.parents[self.find(x)] = self.find(y)


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        def is_similar(w1: str, w2: str) -> bool:
            return sum(a != b for a, b in zip(w1, w2)) <= 2

        N, W = len(strs), len(strs[0])
        dsu = DSU(N)

        if N < W * W:  # If less words.
            for (i1, w1), (i2, w2) in combinations(enumerate(strs), 2):
                if is_similar(w1, w2):
                    dsu.union(i1, i2)

        else:  # If less word length.
            memo = defaultdict(set)
            for i1, s in enumerate(strs):
                l = list(s)
                for j1, j2 in combinations(range(W), 2):
                    l[j1], l[j2] = l[j2], l[j1]
                    memo[''.join(l)].add(i1)
                    l[j1], l[j2] = l[j2], l[j1]

            for i1, s in enumerate(strs):
                for i2 in memo[s]:
                    dsu.union(i1, i2)

        return sum(dsu.parents[x] == x for x in range(N))
