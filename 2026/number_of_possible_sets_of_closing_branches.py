"""
https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/description/
"""


from copy import deepcopy


class Solution:
    """
    Solution
    """

    def number_of_sets(self, n: int, max_distance: int, roads: list[list[int]]) -> int:
        """
        number of sets
        """
        def check(mask: int, g: list[list[int]]) -> int:
            for k in range(n):
                if mask & (1 << k):
                    for l in range(n):
                        if mask & (1 << l):
                            for r in range(n):
                                if mask & (1 << r):
                                    g[l][r] = min(
                                        g[l][r],
                                        g[l][k] + g[k][r]
                                    )

            for u in range(n):
                if mask & (1 << u):
                    for v in range(n):
                        if mask & (1 << v) and g[u][v] > max_distance:
                            return 0

            return 1

        g = [[10 ** 4] * n for _ in range(n)]

        for u in range(n):
            g[u][u] = 0

        for u, v, w in roads:
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)

        return 1 + sum(
            check(mask, deepcopy(g))
            for mask in range(1, 1 << n)
        )
