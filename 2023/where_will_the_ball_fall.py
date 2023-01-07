"""
https://leetcode.com/problems/where-will-the-ball-fall/
"""


from collections import deque


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        R, C = len(grid), len(grid[0])
        queue = deque([(c, 0, c) for c in range(C)])
        rslt = [None] * C
        while queue:
            originalCol, currRow, currCol = queue.popleft()
            if (
                (
                    grid[currRow][currCol] == 1 and
                    (
                        currCol + 1 == C or grid[currRow][currCol + 1] != 1
                    )
                ) or
                (
                    grid[currRow][currCol] == -1 and
                    (
                        currCol == 0 or grid[currRow][currCol - 1] != -1
                    )
                )
            ):
                # Hit the wall or reach the bottom of the V valley.
                rslt[originalCol] = -1
            elif currRow + 1 == R:
                # fall out of the box.
                rslt[originalCol] = currCol + grid[currRow][currCol]
            else:
                queue.append(
                    (
                        originalCol,
                        currRow + 1,
                        currCol + grid[currRow][currCol]
                    )
                )

        return rslt


print(Solution().findBall(
    [
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1]
    ]
))
