"""
https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # Search row.
        row = self.binary_search(
            [matrix[i][0] for i in range(len(matrix))], target)
        if row >= 0:
            if matrix[row][0] == target:
                return True

            # Search column.
            col = self.binary_search(matrix[row], target)
            if col >= 0:
                if matrix[row][col] == target:
                    return True

        return False

    def binary_search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if target < nums[0]:
            return -1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m

        return r  # When target > nums[-1].


matrix = [[1, 3]]
print(Solution().searchMatrix(matrix, 3))
