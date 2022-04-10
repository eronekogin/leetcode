"""
https://leetcode.com/problems/bus-routes/
"""


from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(
            self, routes: list[list[int]], source: int, target: int) -> int:
        """
        Consider each bus as a node, and if the routes of two buses shares at
        least one bus stop, they are considered connected in the graph. Then
        we could use BFS to search the shortest path from source to target.
        """
        if source == target:  # Same stop.
            return 0

        queue = deque()
        graph = defaultdict(set)
        routes = list(map(set, routes))
        visited, targets = set(), set()

        # Create the graph based on the input routes.
        N = len(routes)
        for i, r1 in enumerate(routes):
            if source in r1:
                visited.add(i)
                queue.append((i, 1))

            if target in r1:
                targets.add(i)

            for j in range(i + 1, N):
                if r1 & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)

        # Check routes using BFS.
        while queue:
            currNode, cnt = queue.popleft()
            if currNode in targets:
                return cnt

            for neighbor in graph[currNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, cnt + 1))

        return -1  # Not found.
