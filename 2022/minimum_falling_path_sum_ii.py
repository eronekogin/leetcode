"""
https://leetcode.com/problems/minimum-falling-path-sum-ii/
"""


from heapq import nsmallest


class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        """
        1. Find the minimum and the second minimum numbers on each row.
        2. Then for each item, accumulate the result as follows:
            2.1 if minimum number is taken, add the second minimum number as
                the adjacent column should not be the same.
            2.2 Else, add the minimum number.
        """
        N = len(grid)
        for r in range(1, N):
            # Find two smallest elements in the previous row.
            candidates = nsmallest(2, grid[r - 1])
            for c in range(N):
                if grid[r - 1][c] == candidates[0]:
                    grid[r][c] += candidates[1]
                else:
                    grid[r][c] += candidates[0]

        return min(grid[-1])
