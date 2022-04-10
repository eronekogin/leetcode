"""
https://leetcode.com/problems/critical-connections-in-a-network/
"""


from collections import defaultdict


class Solution:
    def criticalConnections(
        self,
        n: int,
        connections: list[list[int]]
    ) -> list[list[int]]:
        def dfs(parentNode: int, currNode: int, depth: int) -> int:
            """
            Visit each edge starting from node to its neighbors and
            return the minimum depth that it can reach.
            """
            if ranks[currNode] >= 0:  # visited
                return ranks[currNode]

            ranks[currNode] = depth
            minDepth = n
            for neighborNode in graph[currNode]:
                if neighborNode == parentNode:
                    continue

                neighborDepth = dfs(currNode, neighborNode, depth + 1)
                if neighborDepth <= depth:
                    edges.discard(tuple(sorted([currNode, neighborNode])))

                minDepth = min(minDepth, neighborDepth)

            return minDepth

        ranks = [-1] * n

        # Build graph.
        graph = defaultdict(list)
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)

        # Sort edges.
        edges = set(map(tuple, map(sorted, connections)))

        # Scan the graph to discard any edges that within a cycle.
        dfs(-1, 0, 0)

        # The remaining edges are critical ones
        return list(map(list, edges))
