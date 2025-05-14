"""
https://leetcode.com/problems/shortest-cycle-in-a-graph/description/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def find_shortest_cycle(self, n: int, edges: list[list[int]]) -> int:
        """
        find shortest cycle
        """
        def bfs(node: int):
            nonlocal min_cycle_len

            distances = [-1] * n
            q = deque([(node, -1)])
            visited[node] = 1
            distances[node] = 0

            while q:
                curr_node, parent = q.popleft()
                d = distances[curr_node]
                for next_node in graph[curr_node]:
                    if next_node == parent:
                        continue

                    if distances[next_node] != -1:
                        min_cycle_len = min(
                            min_cycle_len,
                            distances[next_node] + d + 1
                        )
                        continue

                    distances[next_node] = d + 1
                    q.append((next_node, curr_node))

        visited = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        min_cycle_len = len(edges) + 1
        for node in range(n):
            if visited[node]:
                continue

            bfs(node)

        if min_cycle_len == len(edges) + 1:
            return -1  # No cycle found

        return min_cycle_len
