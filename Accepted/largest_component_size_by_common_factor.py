"""
https://leetcode.com/problems/largest-component-size-by-common-factor/
"""


from typing import List


class DisjointSets:
    """
    Implementation of the disjoint sets, which is used in the
    Union-Find algorithm. The general idea is that we want to represent a
    group of different sets which are disjoint from each other. 
    We could think of each set as a tree and the root of the tree is the
    representative of this set. Then we could perform the below operations
    against the disjoint sets:

    1. Find the root for a specific element. In order to accelerate the search
        operation, we point each element directly to its root instead of its
        nearest parent.
    2. Union two elements:
        2.1 If the elements belong to the same root, no need to union.
        2.2 If the elements belong to different roots, point the root having
            less elements to the root having more. This could also accelarate
            the speed of the find method later.
    """

    def __init__(self, maxSize: int):
        # Initially the root for each element is itself.
        self._roots = [i for i in range(maxSize)]

        # Counts for elements under each set.
        self._counts = [1] * maxSize

    def get_max(self) -> int:
        return max(self._counts)

    def find(self, x: int) -> int:
        if x != self._roots[x]:
            self._roots[x] = self.find(self._roots[x])  # Path compression.

        return self._roots[x]

    def union(self, old: int, new: int) -> None:
        ro, rn = self.find(old), self.find(new)
        if ro != rn:  # Union the shorter tree to the taller tree.
            if self._counts[ro] > self._counts[rn]:
                self._roots[rn] = ro
                self._counts[ro] += self._counts[rn]
            else:
                self._roots[ro] = rn
                self._counts[rn] += self._counts[ro]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def process_factor(factor: int) -> None:
            if factor not in memo:
                memo[factor] = i
            else:
                ds.union(memo[factor], i)

        ds = DisjointSets(len(A))

        # {factor: index of the number in A where the factor is firstly
        # occurred as a factor of the number}.
        memo = {}
        for i, num in enumerate(A):
            # If f is a factor of num, then num // f is also a factor of num.
            # Since (f, num//f) is the same as (num//f, f), we only need to
            # check the left half where f <= num // f, which then gives us
            # the range [2, num**0.5 + 1) as we want to find a common factor
            # greater than 1.
            for f in range(2, int(num**0.5) + 1):
                if not num % f:  # f is a factor of num.
                    process_factor(f)
                    process_factor(num // f)

            # num itself could be a factor for other larger number, so we need
            # to process it as well.
            process_factor(num)

        return ds.get_max()


print(Solution().largestComponentSize(
    [84, 171, 548, 709, 455, 967, 328, 779,
     79, 16, 168, 675, 276, 473, 697, 26, 731, 668, 634, 607]))
