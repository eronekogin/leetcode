"""
https://leetcode.com/problems/maximum-difference-score-in-a-grid/description/
"""


class Solution:
    """
    Solution
    """

    def max_score(self, grid: list[list[int]]) -> int:
        """
        from any start point c0 to any of the end point ck
        at its bottom and right through a list of points
        c0, c1, c2, ..., ck, the total cost is
        c1 - c0 + c2 - c1 + ... + ck - cy = ck - c0
        """
        max_cost = 10 ** 6
        rslt = -max_cost
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                prev = min(
                    grid[r - 1][c] if r else max_cost,
                    grid[r][c - 1] if c else max_cost
                )
                rslt = max(rslt, v - prev)
                grid[r][c] = min(v, prev)

        return rslt
