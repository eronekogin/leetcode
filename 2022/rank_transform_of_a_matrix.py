"""
https://leetcode.com/problems/rank-transform-of-a-matrix/
"""


from collections import defaultdict


class DSU:
    def __init__(self):
        self.parents: dict[int, int] = {}

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int):
        self.parents.setdefault(x, x)
        self.parents.setdefault(y, y)
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parents[px] = py

    def get_groups(self):
        rslt: defaultdict[int, list[int]] = defaultdict(list)
        for i in self.parents.keys():
            rslt[self.find(i)].append(i)

        return rslt.values()


class Solution:
    """
    1. For cells having the same values, if they are sharing a common row or
        column, they must have the same rank.
    2. So we could use union find to group those cells, and the rank of them
        are the maximum rank of all the rows and cols included.
    """

    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        R, C = len(matrix), len(matrix[0])
        memo: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                memo[v].append((r, c))

        ranks = [0] * (R + C)
        for v in sorted(memo):
            dsu = DSU()
            for r, c in memo[v]:
                # c + R is to differenciate the case when r == c, so that we
                # don't get an invalid union.
                dsu.union(r, c + R)

            for group in dsu.get_groups():
                maxRank = max(ranks[i] for i in group)
                nextRank = maxRank + 1
                for i in group:
                    ranks[i] = nextRank

            for r, c in memo[v]:
                matrix[r][c] = ranks[r]

        return matrix
