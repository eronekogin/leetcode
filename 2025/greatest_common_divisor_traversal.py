"""
https://leetcode.com/problems/greatest-common-divisor-traversal/description/
"""


class DSU:
    """
    Disjoint Set Union
    """

    def __init__(self, size: int) -> None:
        self.parents = list(range(size + 1))
        self.ranks = [1] * (size + 1)

    def find(self, x: int) -> int:
        """
        find parent
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        """
        union x into y
        """
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.ranks[px] > self.ranks[py]:
            px, py = py, px

        self.parents[px] = py
        self.ranks[py] += self.ranks[px]


class Solution:
    """
    Solution
    """

    def can_traverse_all_pairs(self, nums: list[int]) -> bool:
        """
        can traverse all pairs
        """
        max_num = max(nums)
        n = len(nums)
        exists_flags = [False] * (max_num + 1)

        for x in nums:
            exists_flags[x] = True

        if n == 1:
            return True

        if exists_flags[1]:  # We can never reach node 1.
            return False

        sieve = [0] * (max_num + 1)
        for i in range(2, max_num + 1):
            if sieve[i] == 0:
                for j in range(i, max_num + 1, i):
                    sieve[j] = i

        dsu = DSU(2 * max_num + 1)
        for x in nums:
            curr = x
            while curr > 1:
                p = sieve[curr]
                root = p + max_num
                if dsu.find(root) != dsu.find(x):
                    dsu.union(root, x)

                while curr % p == 0:
                    curr //= p

        return sum(
            exists_flags[i] and dsu.find(i) == i
            for i in range(2, max_num + 1)
        ) == 1
