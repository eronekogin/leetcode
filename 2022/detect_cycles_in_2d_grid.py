"""
https://leetcode.com/problems/detect-cycles-in-2d-grid/
"""


class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        def dfs(currNode: tuple[int], parentNode: tuple[int]) -> bool:
            if currNode in visited:  # Found cycle.
                return True

            visited.add(currNode)
            r, c = currNode
            target = grid[r][c]
            candidates = [
                (nr, nc)
                for nr, nc in [
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1)
                ]
                if (
                    0 <= nr < R and
                    0 <= nc < C and
                    grid[nr][nc] == target and
                    (nr, nc) != parentNode
                )
            ]

            return any(dfs(node, currNode) for node in candidates)

        R, C = len(grid), len(grid[0])
        visited: set[tuple[int]] = set()
        for r in range(R):
            for c in range(C):
                if (r, c) in visited:
                    continue

                if dfs((r, c), (-1, -1)):
                    return True

        return False
