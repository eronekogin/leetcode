"""
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
"""


from collections import defaultdict
from math import ceil


class Solution:
    """
    Solution
    """

    def minimum_fuel_cost(self, roads: list[list[int]], seats: int) -> int:
        """
        minimum fuel cost
        """
        def dfs(curr_node: int, prev_node: int, people=1):
            nonlocal cost

            for next_node in graph[curr_node]:
                if next_node == prev_node:
                    continue

                people += dfs(next_node, curr_node)

            cost += ceil(people / seats) if curr_node else 0
            return people

        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        cost = 0
        dfs(0, 0)
        return cost


print(Solution().minimum_fuel_cost(
    [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2))
