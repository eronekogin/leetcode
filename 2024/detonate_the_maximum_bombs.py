"""
https://leetcode.com/problems/detonate-the-maximum-bombs/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def maximum_detonation(self, bombs: list[list[int]]) -> int:
        """
        maximum_detonation
        """
        def dfs(node: int, visited: set[int]):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        n = len(bombs)
        rslt = 0

        # Build graph
        graph: defaultdict[int, list[int]] = defaultdict(list)
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    graph[i].append(j)

        # dfs each node.
        for i in range(n):
            visited = {i}
            dfs(i, visited)
            rslt = max(rslt, len(visited))

        return rslt
