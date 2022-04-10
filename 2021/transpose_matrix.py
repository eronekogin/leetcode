"""
https://leetcode.com/problems/transpose-matrix/
"""


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        After transpose, all rows become columns now and all columns
        become all rows now.
        """
        R, C = len(matrix), len(matrix[0])
        return [[matrix[r][c] for r in range(R)] for c in range(C)]

    def transpose2(self, matrix: list[list[int]]) -> list[list[int]]:
        return list(zip(*matrix))


print(Solution().transpose2([[1, 2, 3], [4, 5, 6]]))
