"""
https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description/
"""


from itertools import permutations


class Solution:
    """
    Solution
    """

    def minimum_moves(self, grid: list[list[int]]) -> int:
        """
        minimum moves
        """
        def calc_distance(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        zeros: list[tuple[int, int]] = []
        spares: list[tuple[int, int]] = []

        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 0:
                    zeros.append((r, c))
                elif v > 1:
                    spares.extend([(r, c)] * (v - 1))

        return min(
            sum(calc_distance(*x, *y) for x, y in zip(zeros, pers))
            for pers in set(permutations(spares))
        )
