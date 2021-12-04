"""
https://leetcode.com/problems/as-far-from-land-as-possible/
"""


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """
        Use BFS to search starting at each island node and try to reach any
        new water nodes until no new water nodes could be reached.
        """
        R, C = len(grid), len(grid[0])
        currLevel = 0
        currNodes = [
            (r, c)
            for r, row in enumerate(grid)
            for c, v in enumerate(row)
            if v
        ]
        if not currNodes or len(currNodes) == R * C:  # 0 or all islands
            return -1

        visited = set(currNodes)
        while currNodes:
            nextNodes = []
            for r, c in currNodes:
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if (
                        0 <= nr < R
                        and 0 <= nc < C
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 0
                    ):
                        visited.add((nr, nc))
                        nextNodes.append((nr, nc))

            currLevel += 1
            currNodes = nextNodes

        return currLevel - 1
