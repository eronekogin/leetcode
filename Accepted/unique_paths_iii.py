"""
https://leetcode.com/problems/unique-paths-iii/
"""


from typing import List


class Solution:
    def __init__(self):
        self._pathCnt = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def walk(currCnt: int, r: int, c: int) -> None:
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] < 0:
                return

            if grid[r][c] == 2:  # Arrived at the end.
                if currCnt == emptyCnt:  # Has walked every empty cells.
                    self._pathCnt += 1

                return

            # Arrived at a middle cell.
            originVal = grid[r][c]
            grid[r][c] = -2  # Mark the current cell visited.

            # Walk towards its four adjacent cells.
            nextCnt = currCnt + 1
            walk(nextCnt, r - 1, c)
            walk(nextCnt, r + 1, c)
            walk(nextCnt, r, c - 1)
            walk(nextCnt, r, c + 1)

            grid[r][c] = originVal  # Restore the current cell value.

        if not grid or not grid[0]:  # Grid is empty.
            return 0

        R, C = len(grid), len(grid[0])

        # Count the empty cells and find the start cell.
        emptyCnt = 0
        start = None
        for r in range(R):
            for c in range(C):
                if not grid[r][c]:
                    emptyCnt += 1
                elif grid[r][c] == 1:
                    start = (r, c)

        if not start:  # No start point.
            return 0

        walk(-1, *start)
        return self._pathCnt


print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
