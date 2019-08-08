"""
https://leetcode.com/problems/n-queens-ii/
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def place_next_queen(
                placedQueens: List[int],
                diffs: List[int],
                sums: List[int]) -> int:
            """
            Use DFS method to place each queen:

            placedQueens is a list used to store the poisiton of the placed
            queens. The index stands for the row and the value stands for the
            column of the placed queen.

            diffs stands for the diagnoal with y = x + b.
            sums stands for the diagnoal with y = -x + b.

            So to prevent each two queen to not attack each other, the new
            queen should not be placed at:

            1. On the same column.
            2. On the same diagnol.
            """
            currRow = len(placedQueens)
            if currRow == n:  # Found a solution.
                return 1

            cnt = 0
            for currCol in range(n):
                currDiff, currSum = currRow - currCol, currRow + currCol
                if currCol not in placedQueens \
                        and currDiff not in diffs and currSum not in sums:
                    # Found a good position to place the current queen.
                    cnt += place_next_queen(
                        placedQueens + [currCol],
                        diffs + [currDiff],
                        sums + [currSum])

            return cnt

        return place_next_queen([], [], [])


print(Solution().solveNQueens(4))
