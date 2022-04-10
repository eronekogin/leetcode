"""
https://leetcode.com/problems/transform-to-chessboard/
"""


from collections import Counter


class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        """
        1. For a valid chessboard:
            1.1 Each row should be the same or inverse of the first row.
            1.2 Each column should be the same or inverse of the first column.
            1.3 The difference between the total occurrences of the two unique
                rows should be no greater than 1. In other words:
                1.3.1 When the board has even number of rows, the total
                    occurrences of the two unique row should be the same.
                1.3.2 When the board has odd number of rows, one unique row
                    should have 1 more occurrence than the other.
            1.4 For the first row:
                1.4.1 If the board has even number of columns, the total
                    occurrences of 0 and 1 should be the same.
                1.4.2 If the board has odd number of columnns, the difference
                    between the total occurrences of 0 and 1 should be 1.
        2. Then in order to swap minumum times:
            2.1 We first compare the difference between the original row and
                the row starting with 0 and store it as rDiffCnt.
            2.2 If the board contains even number of columns, we simply choose
                the smaller swap times from rDiffCnt and N - rDiffCnt. Notice
                that N - rDiffCnt means we swap the board in a reverse way.
            2.3 If the board contains odd number of columns:
                2.3.1 If rDiffCnt is odd, then we will take N - rDiffCnt
                    as N - rDiffCnt must be less than rDiffCnt.
                2.3.2 If rDiffCnt is even, then we will take rDiffCnt.
        3. Similar as column.
        4. Since we swap two rows or two columns at the same time in one swap,
            the final result will be the half of the sum of those difference
            counters. 
        """
        N = len(board)
        rowCnt = Counter(''.join(map(str, row)) for row in board)
        if len(rowCnt) != 2:
            return -1

        r1, r2 = rowCnt.keys()
        if abs(rowCnt[r1] - rowCnt[r2]) > 1 or \
                abs(len(r1) - (r1.count('0') << 1)) > 1 or \
                any(c1 == c2 for c1, c2 in zip(r1, r2)):
            return -1

        rDiffCnt = sum(board[0][c] != c & 1 for c in range(N))
        cDiffCnt = sum(board[r][0] != r & 1 for r in range(N))

        if not N & 1:
            rDiffCnt = min(rDiffCnt, N - rDiffCnt)
            cDiffCnt = min(cDiffCnt, N - cDiffCnt)
        else:
            if rDiffCnt & 1:
                rDiffCnt = N - rDiffCnt

            if cDiffCnt & 1:
                cDiffCnt = N - cDiffCnt

        return (rDiffCnt + cDiffCnt) >> 1
