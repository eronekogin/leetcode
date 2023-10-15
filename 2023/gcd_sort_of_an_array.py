"""
https://leetcode.com/problems/gcd-sort-of-an-array/
"""


class DSU:
    """
    Disjoint Set Union.
    """

    def __init__(self):
        self.parents: dict[int, int] = {}

    def find(self, x: int):
        """
        Find x's parent.
        """
        if self.parents.setdefault(x, x) != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int):
        """
        Union x and y.
        """
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parents[px] = py


class Solution:
    """
    Solution.
    """

    def gcd_sort(self, nums: list[int]) -> bool:
        """
        * General idea is to have the original list sorted, then compare each pair at any index i
            to see if we can swap them.
        * In order to check if we can swap them, we need to check if they share the gcd greather
            than 1. We can first calculate those prime factors, and link the taget numbers to
            the prime factor for later check.
        """
        def get_smallest_prime_factors(x: int):
            """
            Get smallest prime factors for x.
            """
            spf = list(range(x))
            for i in range(2, x):
                if spf[i] != i:
                    continue

                for j in range(i * i, x, i):
                    if spf[j] > i:
                        spf[j] = i

            return spf

        def get_prime_factors(x: int, spf: list[int]):
            """
            Calculate all prime factors for x.
            """
            while x > 1:
                yield spf[x]
                x //= spf[x]

        spf = get_smallest_prime_factors(max(nums) + 1)
        dsu = DSU()
        for x in nums:
            for f in get_prime_factors(x, spf):
                dsu.union(x, f)

        for x, y in zip(nums, sorted(nums)):
            if dsu.find(x) != dsu.find(y):
                return False

        return True
