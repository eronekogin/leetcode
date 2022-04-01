"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
"""


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        C = len(grid[0])
        cnt = 0
        for row in grid:
            for c, v in enumerate(row):
                if v < 0:
                    cnt += C - c
                    break

        return cnt
