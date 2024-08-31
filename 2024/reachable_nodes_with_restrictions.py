"""
https://leetcode.com/problems/reachable-nodes-with-restrictions/description/
"""


class Solution:
    """
    Solution
    """

    def reachable_nodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        """
        reachable nodes
        """
        cannot_pass = set(restricted)
        graph: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited: set[int] = {0}
        queue: list[int] = [0]
        for curr in queue:
            for node in graph[curr]:
                if node in cannot_pass or node in visited:
                    continue

                visited.add(node)
                queue.append(node)

        return len(visited)
