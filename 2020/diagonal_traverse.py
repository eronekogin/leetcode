"""
https://leetcode.com/problems/diagonal-traverse/
"""


from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        dr, dc = -1, 1  # Initially toward the up-right direction.
        R, C = len(matrix) - 1, len(matrix[0]) - 1
        rslt = [matrix[0][0]]
        r = c = 0
        while r != R or c != C:  # Not the last item.
            # Calculate the next item.
            r += dr
            c += dc

            # 1. When r = -1 and c = C + 1, we follow the column handling.
            # 2. When r = R + 1 and c = -1, we follow the row handling.
            if (r < 0 or r > R) and c <= C:  # r is out of boundary.
                c += 1
                dr, dc = -dr, -dc
                r += dr
                c += dc
            elif c < 0 or c > C:  # c is out of boundary.
                r += 1
                dr, dc = -dr, -dc
                r += dr
                c += dc

            rslt.append(matrix[r][c])

        return rslt


print(Solution().findDiagonalOrder(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
))
