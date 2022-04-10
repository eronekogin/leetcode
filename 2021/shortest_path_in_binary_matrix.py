"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""


from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:  # Either start or end cell is not zero.
            return -1

        queue = deque([(1, 0, 0)])
        visited = {(0, 0)}
        N = len(grid) - 1
        while queue:
            pathLen, r, c = queue.popleft()
            if r == c == N:
                return pathLen
            else:
                for nr, nc in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                               (r, c - 1), (r, c + 1), (r + 1, c - 1),
                               (r + 1, c), (r + 1, c + 1)]:
                    if 0 <= nr <= N and 0 <= nc <= N and not grid[nr][nc] and \
                            (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((pathLen + 1, nr, nc))

        return -1  # Could not be found.


print(Solution().shortestPathBinaryMatrix(
    [[0, 1], [1, 0]]
))
