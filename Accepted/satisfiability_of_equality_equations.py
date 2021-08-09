"""
https://leetcode.com/problems/satisfiability-of-equality-equations/
"""

from string import ascii_lowercase


class DSU:
    def __init__(self) -> None:
        self.parents = [x for x in range(26)]

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        self.parents[self.find(x)] = self.find(y)


class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        equals = [item for item in equations if item[1] == '=']
        notEquals = [item for item in equations if item[1] == '!']
        dsu = DSU()
        memo = {c: i for i, c in enumerate(ascii_lowercase)}

        # Build dsu.
        for item in equals:
            x, y = item[0], item[-1]
            dsu.union(memo[x], memo[y])

        # Check unequal conflict.
        for item in notEquals:
            x, y = item[0], item[-1]
            if dsu.find(memo[x]) == dsu.find(memo[y]):
                return False  # Found conflict.

        return True
