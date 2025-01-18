"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
"""


from collections import defaultdict, deque


class Solution:
    """
    Solution
    """

    def min_score(self, n: int, roads: list[list[int]]) -> int:
        """
        min score
        """
        graph: defaultdict[int, dict[int, int]] = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        visited: set[int] = set()
        queue: deque[int] = deque([1])
        min_score = 10 ** 5
        while queue:
            curr_node = queue.popleft()
            for next_node, w in graph[curr_node].items():
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)

                min_score = min(min_score, w)

        return min_score
