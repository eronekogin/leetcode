"""
https://leetcode.com/problems/minimum-cost-for-tickets/
"""


from typing import List
from bisect import bisect_left


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Simple dfs with cache. On the ith travel day, the traveller has three
        choices and we need to determine the minimum cost from there.
        Meanwhile we use binary search in days to determine the nearest next
        travel day when the traveller has to buy a new ticket.
        """
        def calc_cost(start: int) -> int:
            if start >= n:  # No more cost after the last travel day.
                return 0

            if start not in memo:
                memo[start] = min(
                    cost + calc_cost(
                        bisect_left(days, days[start] + duration, start))
                    for cost, duration in tickets)

            return memo[start]

        n, tickets, memo = len(days), list(zip(costs, [1, 7, 30])), {}
        return calc_cost(0)


print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
