"""
https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/description/
"""


class Solution:
    """
    Solution
    """

    def is_possible(self, n: int, edges: list[list[int]]) -> bool:
        """
        is possible
        """
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)

        odd_nodes = [i for i in range(n) if len(graph[i]) & 1]

        if len(odd_nodes) == 2:
            a, b = odd_nodes
            return any(a not in graph[i] and b not in graph[i] for i in range(n))

        if len(odd_nodes) == 4:
            a, b, c, d = odd_nodes
            return (
                (a not in graph[b] and c not in graph[d]) or
                (a not in graph[c] and b not in graph[d]) or
                (a not in graph[d] and c not in graph[b])
            )

        return len(odd_nodes) == 0
