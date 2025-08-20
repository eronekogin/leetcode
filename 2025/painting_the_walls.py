"""
https://leetcode.com/problems/painting-the-walls/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def paint_walls(self, cost: list[int], time: list[int]) -> int:
        """
        paint walls
        """
        @cache
        def dp(curr: int, remain_walls: int) -> int:
            if remain_walls <= 0:
                return 0

            if curr == n:
                return 10 ** 9

            hire_paid_cost = (
                cost[curr] + dp(curr + 1, remain_walls - 1 - time[curr])
            )

            no_hire_cost = dp(curr + 1, remain_walls)
            return min(hire_paid_cost, no_hire_cost)

        n = len(cost)
        return dp(0, n)
