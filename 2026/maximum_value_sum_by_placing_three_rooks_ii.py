"""
https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/description/
"""


from heapq import nlargest
from itertools import chain, combinations


class Solution:
    """
    Solution
    """

    def maximum_value_sum(self, board: list[list[int]]) -> int:
        """
        maximum value sum
        """
        m, n = len(board), len(board[0])

        rows = [
            nlargest(3, [(board[r][c], r, c) for c in range(n)])
            for r in range(m)
        ]

        cols = [
            nlargest(3, [(board[r][c], r, c) for r in range(m)])
            for c in range(n)
        ]

        s = nlargest(11, set(chain(*rows)) & set(chain(*cols)))

        return max(
            sum(a[0] for a in c)
            for c in combinations(s, 3)
            if len({a[1] for a in c}) == 3 and len({a[2] for a in c}) == 3
        )
