"""
https://leetcode.com/problems/maximum-star-sum-of-a-graph/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def max_star_sum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        """
        max star sum
        """
        graph = defaultdict(list)
        for u, v in edges:
            if vals[v] > 0:
                graph[u].append(v)

            if vals[u] > 0:
                graph[v].append(u)

        max_sum = -10 ** 5
        for curr_node, val in enumerate(vals):
            curr_vals = [vals[node] for node in graph[curr_node]]
            curr_vals.sort(reverse=True)
            max_sum = max(max_sum, val + sum(curr_vals[:k]))

        return max_sum
