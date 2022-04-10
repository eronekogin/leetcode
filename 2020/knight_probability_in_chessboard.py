"""
https://leetcode.com/problems/knight-probability-in-chessboard/
"""


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        """
        1. Suppose f[r][c][s] is the possibility to reach cell (r, c)
            after s steps. Then we have:
                f[r][c][s] = sum(f[r + dr][c + dc][s - 1] / 8.0).
        2. Then our problem is to find 
            sum(f[r][c][K] for r in range(N) for c in range(N)).
        3. Since the equation of f is only related to the f[s] and f[s - 1], we
            could reduce the 3d dp list to 2d instead.
        """
        currDp = [[0] * N for _ in range(N)]
        currDp[r][c] = 1
        DIRECTIONS = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for _ in range(K):
            nextDp = [[0] * N for _ in range(N)]
            for cr in range(N):
                for cc in range(N):
                    val = currDp[cr][cc]
                    if val > 0:  # Is able to reach here.
                        for dr, dc in DIRECTIONS:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < N and 0 <= nc < N:  # Still on board.
                                nextDp[nr][nc] += val / 8.0

            currDp = nextDp

        return sum(sum(row) for row in currDp)


print(Solution().knightProbability(3, 2, 0, 0))
