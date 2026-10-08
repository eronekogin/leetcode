"""
https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def shortest_distance_after_queries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        shortest distance after queries
        """
        g = [[i + 1] for i in range(n - 1)]
        g.append([])

        ans = []

        for u, v in queries:
            g[u].append(v)

            # BFS from city 0
            queue = deque([(0, 0)])  # (node, distance)
            visited = {0}

            while queue:
                curr, dist = queue.popleft()
                if curr == n - 1:
                    ans.append(dist)
                    break

                for neighbor in g[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return ans
