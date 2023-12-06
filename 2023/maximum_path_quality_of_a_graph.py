"""
https://leetcode.com/problems/maximum-path-quality-of-a-graph/
"""


from collections import defaultdict


class Solution:
    """
    Solutionn
    """

    def maximal_path_quality(
        self,
        values: list[int],
        edges: list[list[int]],
        max_time: int
    ) -> int:
        """
        maximal_path_quality
        """
        graph = defaultdict(list)
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))

        def dfs(node, visited, gain, cost):
            if node == 0:
                self.ans = max(self.ans, gain)
            for neib, w in graph[node]:
                if w <= cost:
                    dfs(neib, visited | set(
                        [neib]), gain + (neib not in visited) * values[neib], cost - w)

        self.ans = 0
        dfs(0, set([0]), values[0], max_time)
        return self.ans
