"""
https://leetcode.com/problems/minimum-path-cost-in-a-grid/description/
"""


class Solution:
    """
    Solution
    """

    def min_path_cost(self, grid: list[list[int]], move_cost: list[list[int]]) -> int:
        """
        min path cost
        """
        m = len(grid)
        curr_row = [[x, x] for x in grid[0]]

        for r in range(1, m):
            next_row = [[x, 10 ** 6] for x in grid[r]]
            for x, prev_cost in curr_row:
                for c, curr_cost in enumerate(move_cost[x]):
                    next_row[c][1] = min(
                        next_row[c][1],
                        prev_cost + curr_cost + next_row[c][0]
                    )

            curr_row = next_row

        return min(x for _, x in curr_row)
