"""
https://leetcode.com/problems/count-good-triplets-in-an-array/description/
"""


class BIT:
    """
    Binary Indexed Tree, or Fenwick Tree
    """

    def __init__(self, n: int) -> None:
        self.sums = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        """
        update sum of node i and all its children
        """
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)  # Go down to its children

    def query(self, i: int) -> int:
        """
        query sum of subarray from 0 to i
        """
        rslt = 0
        while i > 0:
            rslt += self.sums[i]
            i -= i & (-i)  # Go up to its ancenstor

        return rslt


class Solution:
    """
    Solution
    """

    def good_triplets(self, nums1: list[int], nums2: list[int]) -> int:
        """
        good triplets
        """
        memo = {x: i for i, x in enumerate(nums1)}
        n = len(nums1)
        bit1 = BIT(n)
        bit2 = BIT(n)
        rslt = 0
        for x in nums2:
            i = memo[x]

            # Count how many good triplets ending with i.
            rslt += bit2.query(i)

            # Update for next single node.
            bit1.update(i + 1, 1)

            # Cout how many pairs are less than node i.
            less = bit1.query(i)

            # Update for pairs.
            bit2.update(i + 1, less)

        return rslt
