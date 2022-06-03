"""
https://leetcode.com/problems/diagonal-traverse-ii/
"""


from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        """
        1. For elements on the same diagonal, their row + col are equal to each
            other.
        2. Then we could put the elements with same row + col into a bucket.
        3. Since we collect the cells from the first row to the bottom row,
            when write to result, we need to output elements in reverse order.
        """
        buckets = defaultdict(list)
        for r, row in enumerate(nums):
            for c, v in enumerate(row):
                buckets[r + c].append(v)

        rslt: list[int] = []
        for k in sorted(buckets.keys()):
            rslt.extend(reversed(buckets[k]))

        return rslt


print(Solution().findDiagonalOrder(
    [[14, 12, 19, 16, 9], [13, 14, 15, 8, 11], [11, 13, 1]]))
