"""
https://leetcode.com/problems/triangle/
"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if not n:  # Empty triangle.
            return 0

        currRow = [0] * n
        currRow[0] = triangle[0][0]
        for row in range(1, n):
            # Handle the rightmost.
            currRow[row] = currRow[row - 1] + triangle[row][-1]

            for col in range(row - 1, 0, -1):
                # Handle the middle from right to left.
                currRow[col] = min(
                    currRow[col] + triangle[row][col],
                    currRow[col - 1] + triangle[row][col])

            currRow[0] += triangle[row][0]  # Handle the leftmost.

        return min(currRow)


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(Solution().minimumTotal(triangle))
