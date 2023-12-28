"""
https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
"""


class Solution:
    """
    Solution
    """

    def min_cost(
        self,
        start_pos: list[int],
        home_pos: list[int],
        row_costs: list[int],
        col_costs: list[int]
    ) -> int:
        """
        min_cost
        """
        def cmp(x, y):
            return (x > y) - (x < y)

        min_cost, [x0, y0], [x1, y1] = 0, start_pos, home_pos

        while x0 != x1:
            x0 += cmp(x1, x0)
            min_cost += row_costs[x0]

        while y0 != y1:
            y0 += cmp(y1, y0)
            min_cost += col_costs[y0]

        return min_cost


print(Solution().min_cost([1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]))
