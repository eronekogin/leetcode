"""
https://leetcode.com/problems/maximize-grid-happiness/
"""


from functools import cache


class Solution:
    def getMaxGridHappiness(
        self,
        m: int,
        n: int,
        introvertsCount: int,
        extrovertsCount: int
    ) -> int:
        @cache
        def dp(
            i: int,
            memo: tuple[int],
            intros: int,
            extros: int
        ):
            if intros == extros == 0 or i == total:
                return 0

            up, left = memo[0], memo[-1]

            # Case 1: leave the current cell as blank.
            maxScore = dp(i + 1, memo[1:] + tuple([0]), intros, extros)

            # Case 2: add an introvert to the cell.
            isNotOnLeftBoarder = (i % C) != 0
            if intros:
                score = (
                    120 +
                    mappings[(up, 1)] +
                    isNotOnLeftBoarder * mappings[(left, 1)]
                )
                maxScore = max(
                    maxScore,
                    score + dp(
                        i + 1,
                        memo[1:] + tuple([1]), intros - 1, extros
                    )
                )

            # Case 3: add an extrovert to the cell.
            if extros:
                score = (
                    40 +
                    mappings[(up, 2)] +
                    isNotOnLeftBoarder * mappings[(left, 2)]
                )
                maxScore = max(
                    maxScore,
                    score + dp(
                        i + 1,
                        memo[1:] + tuple([2]), intros, extros - 1
                    )
                )

            return maxScore

        mappings: dict[tuple[int, int], int] = {
            (0, 1): 0,  # Emtpy + intro
            (1, 1): -30 - 30,  # intro + intro
            (2, 1): 20 - 30,  # extro + intro
            (0, 2): 0,  # empty + extro
            (1, 2): -30 + 20,  # intro + extro
            (2, 2): 20 + 20  # extro + extro
        }
        total = m * n
        C, R = sorted([m, n])  # Choose the smaller one for memo cache.
        memo = tuple([0] * C)  # make it a tuple to be cached.
        return dp(0, memo, introvertsCount, extrovertsCount)
