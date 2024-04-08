"""
https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/description/
"""


from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    """
    Solution
    """

    def minimum_weight(
        self,
        n: int,
        edges: list[list[int]],
        src1: int,
        src2: int,
        dest: int
    ) -> int:
        """
        Consider every meet point of the cross path from s1 to dest and from s2 to dest,
        the minimum distance will occur with min(s1, x) + min(s2, x) + min(dest, x)
        """
        def dijkstra(graph: defaultdict[int, list[tuple[int, int]]], src: int):
            heap: list[tuple[int, int]] = [(0, src)]
            dist = [-1] * n
            while heap:
                d, node = heappop(heap)
                if dist[node] == -1:
                    dist[node] = d
                    for v, w in graph[node]:
                        heappush(heap, (d + w, v))

            return dist

        # Build graph.
        g1: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        g2: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

        for u, v, w in edges:
            g1[u].append((v, w))
            g2[v].append((u, w))

        d1 = dijkstra(g1, src1)
        d2 = dijkstra(g1, src2)
        d3 = dijkstra(g2, dest)

        return min(
            [
                d1[i] + d2[i] + d3[i]
                for i in range(n)
                if d1[i] != -1 and d2[i] != -1 and d3[i] != -1
            ] or [-1]
        )
