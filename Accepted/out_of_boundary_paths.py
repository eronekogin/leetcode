"""
https://leetcode.com/problems/out-of-boundary-paths/
"""


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def move(remainSteps: int, r: int, c: int) -> int:
            if not remainSteps:
                return 0

            if r < 0 or r == m or c < 0 or c == n:
                return 1

            if memo[r][c][remainSteps] is None:
                memo[r][c][remainSteps] = \
                    move(remainSteps - 1, r - 1, c) + \
                    move(remainSteps - 1, r + 1, c) + \
                    move(remainSteps - 1, r, c - 1) + \
                    move(remainSteps - 1, r, c + 1)

            return memo[r][c][remainSteps]

        memo = [[[None] * (N + 1) for c in range(n)] for r in range(m)]
        return move(N, i, j) % (10 ** 9 + 7)


print(Solution().findPaths(2, 2, 2, 0, 0))
