"""
https://leetcode.com/problems/modify-graph-edge-weights/description/
"""


from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def modified_graph_edges(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int,
        target: int
    ) -> list[list[int]]:
        """
        modified graph edges
        """
        def djkstra(src: int, dest: int) -> int:
            max_value = 10 ** 11
            distances = [max_value] * n
            distances[src] = 0
            heap = [(0, src)]

            while heap:
                d, u = heappop(heap)
                if d > distances[u]:
                    continue

                for v, w in graph[u]:
                    if d + w < distances[v]:
                        distances[v] = d + w
                        heappush(heap, (d + w, v))

            return distances[dest]

        max_weight = 2 * 10 ** 9
        graph: defaultdict[int, list[list[int]]] = defaultdict(list)
        for u, v, w in edges:
            if w == -1:
                continue

            graph[u].append([v, w])
            graph[v].append([u, w])

        min_distance = djkstra(source, destination)

        if min_distance < target:
            return []

        if min_distance == target:
            # Update all -1 weight edges to maximum weight as result
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = max_weight

            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            edges[i][2] = 1
            graph[u].append([v, 1])
            graph[v].append([u, 1])

            min_distance = djkstra(source, destination)
            if min_distance <= target:
                edges[i][2] += target - min_distance

                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = max_weight

                return edges

        return []
