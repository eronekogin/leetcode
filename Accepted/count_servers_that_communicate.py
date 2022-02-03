"""
https://leetcode.com/problems/count-servers-that-communicate/
"""


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rowCnt = [sum(row) for row in grid]
        colCnt = [sum(col) for col in zip(*grid)]
        return sum(
            rowCnt[r] + colCnt[c] > 2
            for r, row in enumerate(grid)
            for c, hasServer in enumerate(row)
            if hasServer
        )
