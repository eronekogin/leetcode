"""
https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # If the board only have 1 element, consider it has 1 unique path.
        board = [[1] * m for _ in range(n)]

        # The points on the end row or end column have only
        # 1 path, which all goes down or right.
        # Calculate unique paths from the finish point.
        for col in range(m - 2, -1, -1):
            for row in range(n - 2, -1, -1):
                board[row][col] = board[row + 1][col] + board[row][col + 1]

        return board[0][0]


print(Solution().uniquePaths(3, 2))
