"""
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Since all the rows and columns are sorted, starting scanning the
        top right corner:
            1. If the target is greater than the current value, it cannot
                be in the current row.
            2. If the target is less than the current value, it cannot be
                in the current column.
        """
        if not matrix or not matrix[0]:  # Empty matrix.
            return False

        if target < matrix[0][0] or target > matrix[-1][-1]:  # Out of bounds.
            return False

        col = len(matrix[0]) - 1  # Starting at the top right corner.
        for row in matrix:
            while col >= 0 and row[col] > target:
                col -= 1

            if row[col] == target:
                return True

        return False


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().searchMatrix(matrix, 7))
