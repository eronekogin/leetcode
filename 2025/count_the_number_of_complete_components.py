"""
https://leetcode.com/problems/count-the-number-of-complete-components/description/
"""


class Solution:
    """
    Solution
    """

    def count_complete_components(self, n: int, edges: list[list[int]]) -> int:
        """
        count complete components
        """
        degrees = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            graph[u].append(v)
            graph[v].append(u)

        cnt = 0
        visited: set[int] = set()
        for i in range(n):
            if i in visited:
                continue

            path = {i}
            curr_nodes = [i]
            while curr_nodes:
                next_nodes: list[int] = []
                for node in curr_nodes:
                    for neighbor in graph[node]:
                        if neighbor not in path:
                            path.add(neighbor)
                            next_nodes.append(neighbor)

                curr_nodes = next_nodes

            cnt += all(degrees[node] + 1 == len(path) for node in path)
            visited |= path

        return cnt
