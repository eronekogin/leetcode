"""
https://leetcode.com/problems/parallel-courses-iii/
"""


from functools import cache
from collections import defaultdict


class Solution:
    """
    Solution
    """

    def minimum_time(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        """
        minimum_time
        """
        @cache
        def dfs(curr_node: int):
            max_time = max(
                [
                    dfs(next_node)
                    for next_node in graph[curr_node]
                ] or [0]
            )
            return max_time + time[curr_node]

        graph = defaultdict(list)
        for u, v in relations:
            graph[u - 1].append(v - 1)

        return max(dfs(curr_node) for curr_node in range(n))
