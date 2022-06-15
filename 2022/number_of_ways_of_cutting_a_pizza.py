"""
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
"""


from functools import lru_cache


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        @lru_cache(None)
        def cut(remainCuts: int, r: int, c: int) -> int:
            if preSums[r][c] == 0:  # No apple to be cut.
                return 0

            if remainCuts == 0:  # Found a cut solution.
                return 1

            cnt = 0

            # Cut vertically.
            for nc in range(c + 1, C):
                if preSums[r][c] - preSums[r][nc] > 0:
                    cnt = (cnt + cut(remainCuts - 1, r, nc)) % M

            # Cut horizontally.
            for nr in range(r + 1, R):
                if preSums[r][c] - preSums[nr][c] > 0:
                    cnt = (cnt + cut(remainCuts - 1, nr, c)) % M

            return cnt

        R, C = len(pizza), len(pizza[0])
        M = 10 ** 9 + 7

        # Calculate prefix sums.
        preSums = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                preSums[r][c] = (
                    preSums[r][c + 1] +
                    preSums[r + 1][c] -
                    preSums[r + 1][c + 1] +
                    (pizza[r][c] == 'A')
                )

        return cut(k - 1, 0, 0)
