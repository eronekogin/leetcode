"""
https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
"""


from functools import cache


class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        @cache
        def dp(r: int, c: int) -> tuple[int]:
            if r == 0 and c == 0:
                return (grid[r][c], grid[r][c])

            if r < 0 or c < 0:
                return (float('-inf'), float('inf'))

            if grid[r][c] == 0:
                return (0, 0)

            max1, min1 = dp(r - 1, c)
            max2, min2 = dp(r, c - 1)

            currMax = max(max1, max2) * grid[r][c]
            currMin = min(min1, min2) * grid[r][c]

            if grid[r][c] > 0:
                return (currMax, currMin)
            else:
                return (currMin, currMax)

        R, C = len(grid), len(grid[0])
        maxProduct, _ = dp(R - 1, C - 1)
        if maxProduct < 0:
            return -1

        return maxProduct % (10 ** 9 + 7)
