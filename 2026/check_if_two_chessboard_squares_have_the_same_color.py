"""
https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/
"""


class Solution:
    """
    Solution
    """
    def check_two_chessboards(self, coordinate1: str, coordinate2: str) -> bool:
        """
        check two chessboards
        """
        d_col = abs(ord(coordinate1[0]) - ord(coordinate2[0]))
        d_row = abs(int(coordinate1[1]) - int(coordinate2[1]))

        return d_col & 1 == d_row & 1
