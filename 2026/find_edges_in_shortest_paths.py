"""
https://leetcode.com/problems/find-edges-in-shortest-paths/description/
"""


from heapq import heappop, heappush
from math import inf


class Solution:
    """
    Solution
    """

    def find_answer(self, n: int, edges: list[list[int]]) -> list[bool]:
        """
        find answer
        """
        def dj(node: int):
            d = [inf] * n
            d[node] = 0
            heap = [(0, node)]
            while heap:
                curr_distance, curr_node = heappop(heap)
                if d[curr_node] == curr_distance:
                    for next_node, w in g[curr_node]:
                        if curr_distance + w < d[next_node]:
                            d[next_node] = curr_distance + w
                            heappush(heap, (curr_distance + w, next_node))

            return d

        g: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        d0 = dj(0)
        if d0[n - 1] == inf:  # can not reach to n - 1
            return [False] * len(edges)

        dn = dj(n - 1)
        return [
            d0[u] + w + dn[v] == d0[n - 1] or
            d0[v] + w + dn[u] == d0[n - 1]
            for u, v, w in edges
        ]
