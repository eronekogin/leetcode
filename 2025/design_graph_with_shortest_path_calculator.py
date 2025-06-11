"""
https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/
"""


from heapq import heappop, heappush


class Graph:
    """
    Graph
    """

    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = [[] for _ in range(n)]

        for u, v, w in edges:
            self.graph[u].append([v, w])

    def add_edge(self, edge: list[int]) -> None:
        """
        add edge
        """
        u, v, w = edge
        self.graph[u].append([v, w])

    def shortest_path(self, node1: int, node2: int) -> int:
        """
        shortest path
        """
        n = len(self.graph)
        heap = [(0, node1)]
        costs = [10 ** 10] * n
        costs[node1] = 0

        while heap:
            cost, node = heappop(heap)
            if cost > costs[node]:
                continue

            if node == node2:
                return cost

            for next_node, w in self.graph[node]:
                next_cost = cost + w
                if next_cost < costs[next_node]:
                    costs[next_node] = next_cost
                    heappush(heap, (next_cost, next_node))

        return -1
