"""
https://leetcode.com/problems/number-of-islands/
"""


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Use DFS to check the adjacent items when the current item is '1'.
        """
        if not grid:
            return 0

        R, C, islandCnt = len(grid), len(grid[0]), 0
        visitedMemo = [[0] * C for _ in range(R)]

        def check_adjacent(r: int, c: int):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == '0' or\
                    visitedMemo[r][c]:
                return

            visitedMemo[r][c] = 1
            check_adjacent(r + 1, c)
            check_adjacent(r - 1, c)
            check_adjacent(r, c + 1)
            check_adjacent(r, c - 1)

        for r in range(R):
            for c in range(C):
                if not visitedMemo[r][c] and grid[r][c] == '1':
                    check_adjacent(r, c)
                    islandCnt += 1

        return islandCnt
