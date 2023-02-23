"""
https://leetcode.com/problems/map-of-highest-peak/
"""


from collections import deque


class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        def neighbors(r: int, c: int):
            return [
                (nr, nc)
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                if 0 <= nr < R and 0 <= nc < C and heights[nr][nc] == -1
            ]

        R, C = len(isWater), len(isWater[0])
        heights = [[-1] * C for _ in range(R)]
        queue = deque()

        # Fill water cells.
        for r in range(R):
            for c in range(C):
                if isWater[r][c] == 1:
                    heights[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for nr, nc in neighbors(r, c):
                heights[nr][nc] = 1 + heights[r][c]
                queue.append((nr, nc))

        return heights


print(Solution().highestPeak([[0, 1], [0, 0]]))
