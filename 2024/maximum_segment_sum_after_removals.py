"""
https://leetcode.com/problems/maximum-segment-sum-after-removals/description/
"""


class DSU:
    """
    DSU
    """

    def __init__(self) -> None:
        self.parents = {}
        self.sums = {}
        self.max_seg_sum = 0

    def find(self, x: int):
        """
        find
        """
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int):
        """
        union
        """
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        self.sums[px] += self.sums[py]
        self.parents[py] = px
        self.max_seg_sum = max(self.max_seg_sum, self.sums[px])

    def merge(self, x: int, v: int):
        """
        merge
        """
        self.parents[x] = x
        self.sums[x] = v
        self.max_seg_sum = max(self.max_seg_sum, v)

        if x - 1 in self.parents:
            self.union(x, x - 1)

        if x + 1 in self.parents:
            self.union(x, x + 1)


class Solution:
    """
    Solution
    """

    def maximum_segment_sum(self, nums: list[int], remove_queries: list[int]) -> list[int]:
        """
        The last query will remove all the numbers from nums, so we can do it from back to forth
        and merge the sums when adding new numbers
        """
        n = len(nums)
        rslt = [0] * n
        dsu = DSU()

        for i in range(n - 1, -1, -1):
            rslt[i] = dsu.max_seg_sum
            q = remove_queries[i]
            dsu.merge(q, nums[q])

        return rslt
