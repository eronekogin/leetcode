"""
https://leetcode.com/problems/cherry-pickup/
"""


from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def walk(r1: int, c1: int, r2: int, c2: int) -> int:
            if r1 == N or c1 == N or r2 == N or c2 == N:  # Out of grid.
                return -1

            if r1 == r2 == c1 == c2 == N - 1:  # Reach the end.
                return grid[-1][-1]

            if grid[r1][c1] == -1 or grid[r2][c2] == -1:  # Blocked.
                return -1

            if (r1, r2, c1, c2) not in memo:
                cherries = max(
                    walk(r1 + 1, c1, r2, c2 + 1),  # down + right
                    walk(r1 + 1, c1, r2 + 1, c2),  # down + down
                    walk(r1, c1 + 1, r2 + 1, c2),  # right + down
                    walk(r1, c1 + 1, r2, c2 + 1))  # right + right

                if cherries != -1:  # Found new cherries.
                    if r1 == r2 and c1 == c2:
                        cherries += grid[r1][c1]
                    else:
                        cherries += grid[r1][c1] + grid[r2][c2]

                memo[(r1, r2, c1, c2)] = cherries

            return memo[(r1, r2, c1, c2)]

        N, memo = len(grid), {}
        return max(walk(0, 0, 0, 0), 0)


print(Solution().cherryPickup(
    [[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
