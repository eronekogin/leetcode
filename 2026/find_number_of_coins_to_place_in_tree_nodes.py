"""
https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def placed_coins(self, edges: list[list[int]], cost: list[int]) -> list[int]:
        """
        placed coins
        """
        def dp(node: int) -> list[int]:
            coins = [cost[node]]
            cost[node] = 0

            for child in g[node]:
                if cost[child] == 0:
                    continue

                coins.extend(dp(child))

            coins.sort()

            if len(coins) >= 3:
                n1, n2 = coins[:2]
                p3, p2, p1 = coins[-3:]

                # In case the first two items are
                # negative cost, then it could also
                # contribute to the maximum product and that's why
                # we need to check n1 * n2 * p1
                rslt[node] = max(
                    0,
                    n1 * n2 * p1,
                    p1 * p2 * p3
                )

            if len(coins) <= 5:
                return coins

            return [n1, n2, p3, p2, p1]

        rslt = [1] * len(cost)
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        dp(0)

        return rslt
