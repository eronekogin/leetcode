"""
https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_cost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        """
        minimum cost
        """
        def find(x: int) -> int:
            if parents[x] != x:
                parents[x] = find(parents[x])

            return parents[x]

        parents = list(range(n))
        min_path_costs = [-1] * n
        for s, t, w in edges:
            ps = find(s)
            pt = find(t)
            min_path_costs[pt] &= w

            if ps != pt:
                min_path_costs[pt] &= min_path_costs[ps]
                parents[ps] = pt

        rslt: list[int] = []
        for s, t in query:
            if s == t:
                rslt.append(0)
            elif find(s) != find(t):  # Not connected
                rslt.append(-1)
            else:
                rslt.append(min_path_costs[find(s)])

        return rslt
