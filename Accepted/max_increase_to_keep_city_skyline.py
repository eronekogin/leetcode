"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
"""


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        maxRows = [max(row) for row in grid]
        maxCols = [max(col) for col in zip(*grid)]
        return sum(
            min(maxRows[r], maxCols[c]) - v
            for r, row in enumerate(grid)
            for c, v in enumerate(row)
        )


print(Solution().maxIncreaseKeepingSkyline(
    [
        [3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0]
    ]
))
