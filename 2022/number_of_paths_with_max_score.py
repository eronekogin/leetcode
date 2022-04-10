"""
https://leetcode.com/problems/number-of-paths-with-max-score/
"""


class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        """
        dp[r][c] = [x, y], x means the maximum value it can get at (r, c) and
        y means the number of paths that can reach (r, c) from start.
        """
        N = len(board)
        MOD = 10 ** 9 + 7
        dp = [[[-1, 0] for _ in range(N + 1)] for _ in range(N + 1)]
        dp[0][0] = [0, 0]
        dp[N - 1][N - 1] = [0, 1]

        for r in range(N - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if board[r][c] in 'XS':
                    continue

                for nr, nc in [(r, c + 1), (r + 1, c), (r + 1, c + 1)]:
                    if dp[r][c][0] < dp[nr][nc][0]:
                        dp[r][c] = dp[nr][nc][:]
                    elif dp[r][c][0] == dp[nr][nc][0]:
                        dp[r][c][1] += dp[nr][nc][1]

                if r or c:
                    dp[r][c][0] += int(board[r][c])

        if dp[0][0][1]:
            return [dp[0][0][0], dp[0][0][1] % MOD]
        else:
            return [0, dp[0][0][1] % MOD]
