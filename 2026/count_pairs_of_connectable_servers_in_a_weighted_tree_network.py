"""
https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/description/
"""


from collections import defaultdict
from functools import cache


class Solution:
    """
    Solution
    """

    def count_pairs_of_connectable_servers(self, edges: list[list[int]], signal_speed: int) -> list[int]:
        """
        count pairs of connectable servers
        """
        @cache
        def dfs(curr: int, parent: int, path: int) -> int:
            connectable = 1 if path == 0 else 0
            for neighbour, w in g[curr]:
                if neighbour == parent:
                    continue

                connectable += dfs(
                    neighbour,
                    curr,
                    (path + w) % signal_speed
                )

            return connectable

        n = len(edges) + 1
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        rslt = [0] * n

        for root in range(n):
            branches = g[root]
            for i, (a, aw) in enumerate(branches):
                for j in range(i + 1, len(branches)):
                    b, bw = branches[j]
                    rslt[root] += (
                        dfs(a, root, aw % signal_speed) *
                        dfs(b, root, bw % signal_speed)
                    )

        return rslt
