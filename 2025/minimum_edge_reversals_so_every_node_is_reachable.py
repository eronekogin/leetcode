"""
https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def min_edge_reversals(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        min edge reversals
        """
        def dp(parent: int, current: int):
            return sum(
                dp(current, child) + graph[current][child]
                for child in graph[current]
                if child != parent
            )

        def dfs(curr: int, cost=0):
            """
            We already have cost for the current node and we use this to
            calculate the cost of its neighbour node:

            for any neighbour of the current node, the original cost counts
            the cost from curr to neighbour, so we need to subtract graph[curr][child]
            first.

            On the other hand, the new cost now needs to walk from neighbour
            back to the current node, so it needs to add graph[child][curr].
            """
            rslt[curr] = cost
            for child in graph[curr]:
                if rslt[child] < 0:
                    # The cost of the child node has not been calculated yet
                    dfs(child, cost - graph[curr][child] + graph[child][curr])

        graph = defaultdict(dict)
        for u, v in edges:
            graph[u][v] = 0
            graph[v][u] = 1

        rslt = [-1] * n

        dfs(0, dp(-1, 0))
        return rslt
