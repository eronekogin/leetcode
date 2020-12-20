"""
https://leetcode.com/problems/cherry-pickup-ii/
"""


from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        1. Try to move two robots at the same time in order to apply the
            dynamic programming algorithm as if we move 1 robot earlier than
            the other one, the second moved robot's track will depend on the
            first one's.
        2. Suppose dp[r][c1][c2] stands for the maximum cherries both robots
            could get when their starting position is (r, c1) and (r, c2), then
            we have:
            2.1 When both robots are at the bottom row, they don't need to move
                any longer and the collected cherries are the ones lie on the
                bottom row.
            2.2 dp[r-1][c1][c2] = max(dp[r][c1-1], dp[r][c1], dp[r][c1+1],
                dp[r][c2-1], dp[r][c2], dp[r][c2+1]), summarized by the cases
                when both robots could move to three directions.
            2.3 Notice that the previous dp element only depends on the result
                from the next dp element, so we could use the 2D list instead
                of the 3D.
        """
        R, C = len(grid), len(grid[0])
        for r in range(R - 1, -1, -1):
            prev = [[0] * C for _ in range(C)]
            for c1 in range(C):
                for c2 in range(C):
                    prev[c1][c2] = grid[r][c1]
                    if c1 != c2:
                        prev[c1][c2] += grid[r][c2]

                    if r != R - 1:
                        prev[c1][c2] += max(
                            curr[cx][cy]
                            for cx in [c1 - 1, c1, c1 + 1]
                            for cy in [c2 - 1, c2, c2 + 1]
                            if 0 <= cx < C and 0 <= cy < C)

            curr = prev

        return prev[0][-1]
