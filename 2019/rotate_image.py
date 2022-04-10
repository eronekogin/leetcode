"""
https://leetcode.com/problems/rotate-image/
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for r in range(n // 2):
            for c in range(n - n // 2):
                """
                             r, c = 0, 1
                                  |
                                1 2 3 4
                                4 5 6 A -- r, c = 1, -1
                r, c = -2, 0 -- 7 8 9 B
                                C D E F
                                    |
                             r, c = -1, -2
                """
                matrix[r][c], matrix[c][~r], matrix[~r][~c], matrix[~c][r] = (
                    matrix[~c][r], matrix[r][c], matrix[c][~r], matrix[~r][~c]
                )


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Solution().rotate(matrix)
print(matrix)
