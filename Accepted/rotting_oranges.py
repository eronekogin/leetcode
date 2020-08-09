"""
https://leetcode.com/problems/rotting-oranges/
"""


from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        R, C = len(grid), len(grid[0])

        # Collect the initial rotten and fresh orange positions.
        rottens, freshes = set(), set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    rottens.add((r, c))
                elif grid[r][c] == 1:
                    freshes.add((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        totalMinutes = 0
        while freshes:
            if not rottens:
                return -1  # No new rotten ones while still having fresh ones.

            # Calculate new rotten ones.
            rottens = {
                (r + dr, c + dc)
                for r, c in rottens
                for dr, dc in directions
                if (r + dr, c + dc) in freshes}

            freshes -= rottens  # Remove those new rottens from freshes.
            totalMinutes += 1  # Increase time.

        return totalMinutes


print(Solution().orangesRotting([
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]))
