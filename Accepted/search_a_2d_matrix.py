"""
https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # Search row.
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][0]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                return True

        # Search column.
        if r >= 0:
            nums = matrix[r]
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    return True

        return False


matrix = [[1, 3]]
print(Solution().searchMatrix(matrix, 3))
