"""
https://leetcode.com/problems/largest-1-bordered-square/
"""


class Solution:
    def largest1BorderedSquare(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # Calculate number of consecutive 1s on top and left.
        top, left = [row[:] for row in grid], [row[:] for row in grid]
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    if r:  # On top.
                        top[r][c] = top[r - 1][c] + 1

                    if c:  # On left.
                        left[r][c] = left[r][c - 1] + 1

        # From the largest possible size to 1, determine if such square exists.
        for size in range(min(R, C), 0, -1):
            for r in range(R - size + 1):
                for c in range(C - size + 1):
                    if min(
                        top[r + size - 1][c],
                        top[r + size - 1][c + size - 1],
                        left[r][c + size - 1],
                        left[r + size - 1][c + size - 1]
                    ) >= size:
                        return size * size

        # No square found.
        return 0
