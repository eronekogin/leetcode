"""
https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
"""


from collections import defaultdict


class Solution:
    def minTrioDegree(self, n: int, edges: list[list[int]]) -> int:
        """
        1. For each trio, its degree = sum of edges for all the node in this
            trio - 6, 6 means the edges inside this trio.

        2. Since 6 is a fixed value, we can transform the question to compare
            on the sum of edges instead.

        3. So we sort the nodes by its edges in ascending order and start to
            check on the node with minimum edges. If we found the edges of
            the current node is greater than the 1/3 of the current minumum
            total edges, we can immediately break the loop since the sum of
            edges from the remaining nodes must be greater than the current
            minnimum total edges.
        """
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        minTotalEdges = float('inf')
        for u in sorted(range(1, n + 1), key=lambda x: len(graph[x])):
            if len(graph[u]) >= minTotalEdges / 3:
                break

            for v in graph[u]:
                for w in graph[v]:
                    if w in graph[u]:
                        # Found a trio.
                        minTotalEdges = min(
                            minTotalEdges,
                            len(graph[u]) + len(graph[v]) + len(graph[w])
                        )

        if minTotalEdges < float('inf'):
            return minTotalEdges - 6

        return -1  # No trio is found.
