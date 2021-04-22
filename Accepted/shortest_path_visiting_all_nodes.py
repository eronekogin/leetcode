"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/
"""


from collections import deque, defaultdict


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        """
        1. The current walked path could be determined by setting the xth bit
            of an integer to 1 after walking through node x. And the state of
            the walked path could be determined by such an integer together
            with the latest node it has walked through.
        2. Then we perform BFS to walk the neighbor nodes and when we have
            walked through all the nodes, the current length of the walked
            path must be the shortest path.
        """
        N = len(graph)
        WALKED_ALL_NODES = (1 << N) - 1
        queue = deque((1 << x, x) for x in range(N))
        memo = defaultdict(lambda: float('inf'))
        for x in range(N):
            memo[(1 << x, x)] = 0

        while queue:
            currPath, currNode = queue.popleft()
            currLen = memo[(currPath, currNode)]
            if currPath == WALKED_ALL_NODES:
                return currLen

            for nextNode in graph[currNode]:
                nextPath = currPath | (1 << nextNode)
                if currLen + 1 < memo[(nextPath, nextNode)]:
                    memo[(nextPath, nextNode)] = currLen + 1
                    queue.append((nextPath, nextNode))
