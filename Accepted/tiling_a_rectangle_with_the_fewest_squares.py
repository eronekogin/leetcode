"""
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
"""


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        Simple back-tracking solution: always put tiles from left to right and
        from bottom to top and check all combinations to get the minimum move.
        """
        def dfs(heights: list[int], moves: int) -> None:
            if all(h == n for h in heights):
                self.minMoves = min(self.minMoves, moves)
                return

            if moves > self.minMoves:
                return

            minHeight = min(heights)
            start = heights.index(minHeight)
            end = start + 1
            while end < m and heights[end] == minHeight:
                end += 1

            for i in range(min(end - start, n - minHeight), 0, -1):
                newHeights = heights[:]
                for j in range(i):
                    newHeights[start + j] += i

                dfs(newHeights, moves + 1)

        self.minMoves = n * m
        dfs([0] * m, 0)
        return self.minMoves


print(Solution().tilingRectangle(2, 3))
