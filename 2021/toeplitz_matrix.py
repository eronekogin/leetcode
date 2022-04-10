"""
https://leetcode.com/problems/toeplitz-matrix/
"""


from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        1. For any cell in the same diagonal, its r - c should be the same.
            So we could cache the different r - c and match the future result.
        2. This could help when the matrix is huge and we could only load a
            partial of one row into the memory. 
        """
        memo = {}
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                if r - c not in memo:
                    memo[r - c] = v
                elif memo[r - c] != v:
                    return False

        return True
