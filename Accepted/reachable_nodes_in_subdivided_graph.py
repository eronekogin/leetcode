"""
https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
"""


from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def reachableNodes(
            self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        """
        1. Use Dijkstra's algorithm to find all the shortest path to each node
            within maxMoves.
        2. We also need to collect the new nodes used when subdivide each
            edge.
        """
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        heap = [(0, 0)]
        distances = {0: 0}
        used = defaultdict(int)
        rslt = 0

        while heap:
            d, node = heappop(heap)
            if d <= distances[node]:  # Haven't reached this node before.
                rslt += 1
                for neighbor, w in graph[node].items():
                    # maxMoves - d means how much further we could move
                    # from the current node. Then we could determine how many
                    # new nodes we could use in the subdivided edges.
                    used[(node, neighbor)] = min(w, maxMoves - d)

                    # d2 stores the distance in the original graph to reach
                    # to the neighbor node from node 0.
                    d2 = d + w + 1
                    if d2 < distances.get(neighbor, maxMoves + 1):
                        heappush(heap, (d2, neighbor))
                        distances[neighbor] = d2

        # Then for each edge, either we could use all the new nodes in the
        # subdivided edges, or we could use a combination from u to v and
        # v to u.
        for u, v, w in edges:
            rslt += min(w, used[(u, v)] + used[(v, u)])

        return rslt
