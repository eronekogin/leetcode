"""
https://leetcode.com/problems/minimum-moves-to-capture-the-queen/description/
"""


class Solution:
    """
    Solution
    """

    def min_moves_to_capture_the_queen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        """
        if rook and queen are on the same row or same column, it takes one step unless the bishop
        is in the middle, which takes 2 steps to move bishop away first.

        If bishop and queen are on the same diagonal, it takes one step unless the rook is in the
        middle, which takes 2 steps to move rook away first.
        """
        if a == e or b == f:
            if a == e and a == c and (d - b) * (d - f) < 0:
                return 2

            if b == f and b == d and (c - a) * (c - e) < 0:
                return 2

            return 1

        if abs(c - e) == abs(d - f):
            if abs(c - a) == abs(d - b) and abs(e - a) == abs(f - b) and (b - f) * (b - d) < 0:
                return 2

            return 1

        return 2
