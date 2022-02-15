"""
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
"""


from itertools import combinations


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        queue = [(0, 0, 0, 0)]
        visited = {(0, 0, 0)}
        for r, c, obstacleCnt, stepCnt in queue:
            if r + 1 == R and c + 1 == C:
                return stepCnt

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc]:  # Blocked.
                        if (
                            obstacleCnt < k and
                            (nr, nc, obstacleCnt + 1) not in visited
                        ):
                            visited.add((nr, nc, obstacleCnt + 1))
                            queue.append(
                                (nr, nc, obstacleCnt + 1, stepCnt + 1)
                            )
                    else:  # Not blocked.
                        if (nr, nc, obstacleCnt) not in visited:
                            visited.add((nr, nc, obstacleCnt))
                            queue.append((nr, nc, obstacleCnt, stepCnt + 1))

        return -1  # Not possible.
