"""
https://leetcode.com/problems/count-number-of-possible-root-nodes/description/
"""


from collections import defaultdict
from functools import cache


class Solution:
    """
    Solution
    """

    def root_count(self, edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
        """
        root count
        """
        @cache
        def dfs(node: int, parent: int) -> int:
            return sum(
                ((node, next_node) in gt) + dfs(next_node, node)
                for next_node in graph[node]
                if next_node != parent
            )

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        gt = set(map(tuple, guesses))

        return sum(
            dfs(node, -1) >= k
            for node in graph
        )
