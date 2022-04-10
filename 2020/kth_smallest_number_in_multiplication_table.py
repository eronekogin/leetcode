"""
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        Use binary search to search our answer between 1 and m * n.
        """
        l, r = 1, m * n
        while l < r:
            mid = l + ((r - l) >> 1)

            # Check if there are k or more values that are less than mid.
            # For each row, its elements look like 1*i, 2*i, ... n*i, so the
            # largest number that is less than x will be x // i. But if x is
            # too large for the current row, the total count for this row
            # will be n instead.
            if sum(min(mid // r, n) for r in range(1, m + 1)) >= k:
                # mid is our candidate.
                r = mid
            else:
                l = mid + 1

        return l
