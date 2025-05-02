"""
https://leetcode.com/problems/check-knight-tour-configuration/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def check_valid_grid(self, grid: list[list[int]]) -> bool:
        """
        check valid grid
        """
        def is_valid_position(prev: tuple[int, int], curr: tuple[int, int]):
            return {
                abs(prev[0] - curr[0]),
                abs(prev[1] - curr[1])
            } == {1, 2}

        n = len(grid)
        seqs = defaultdict(tuple)

        if n < 5:
            return n == 1

        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                seqs[v] = (r, c)

        prev = (0, 0)
        i = 1
        while i < n * n:
            curr = seqs[i]
            if not is_valid_position(prev, curr):
                return False

            i += 1
            prev = curr

        return True
