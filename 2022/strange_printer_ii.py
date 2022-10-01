"""
https://leetcode.com/problems/strange-printer-ii/
"""


class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        def paint(color: int) -> bool:
            # Check if the color can be painted.
            for r in range(memo[color][0], memo[color][2] + 1):
                for c in range(memo[color][1], memo[color][3] + 1):
                    if targetGrid[r][c] > 0 and targetGrid[r][c] != color:
                        return False

            # Then paint all target cells to zero so that the same color
            # can not be used again.
            for r in range(memo[color][0], memo[color][2] + 1):
                for c in range(memo[color][1], memo[color][3] + 1):
                    targetGrid[r][c] = 0

            return True

        R, C = len(targetGrid), len(targetGrid[0])
        colors: set[int] = set()

        # Initialize positions.
        memo = [[R, C, 0, 0] for _ in range(61)]  # R, C are <= 60.
        for r, row in enumerate(targetGrid):
            for c, color in enumerate(row):
                colors.add(color)
                memo[color][0] = min(memo[color][0], r)
                memo[color][1] = min(memo[color][1], c)
                memo[color][2] = max(memo[color][2], r)
                memo[color][3] = max(memo[color][3], c)

        while colors:
            remainColors: set[int] = set()
            for color in colors:
                if not paint(color):
                    remainColors.add(color)

            if len(remainColors) == len(colors):  # Cannot paint any color.
                return False

            colors = remainColors

        return True
