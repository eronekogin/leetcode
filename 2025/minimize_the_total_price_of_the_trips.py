"""
https://leetcode.com/problems/minimize-the-total-price-of-the-trips/description/
"""


from collections import Counter, defaultdict
from functools import cache


class Solution:
    """
    Solution
    """

    def minimum_total_price(
        self,
        n: int,
        edges: list[list[int]],
        price: list[int],
        trips: list[list[int]]
    ) -> int:
        """
        minimum total price
        """
        def dfs(curr: int, parent: int, end: int):
            nonlocal total_cost
            if curr == end:
                return True

            for neighbor in graph[curr]:
                if neighbor != parent:
                    if dfs(neighbor, curr, end):
                        cnt[neighbor] += 1
                        total_cost += price[neighbor]
                        return True

            return False

        @cache
        def dp(curr: int, parent: int, can_reduce: bool):
            cost = (price[curr] >> 1) * cnt[curr] if can_reduce else 0
            for neighbor in graph[curr]:
                if neighbor != parent:
                    if can_reduce:
                        next_cost = dp(neighbor, curr, False)
                    else:
                        next_cost = max(
                            dp(neighbor, curr, False),
                            dp(neighbor, curr, True)
                        )

                    cost += next_cost

            return cost

        graph: defaultdict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        cnt = Counter()
        total_cost = 0

        # Calculate cost for all trips without reduce any price.
        for start, end in trips:
            cnt[start] += 1
            total_cost += price[start]
            dfs(start, -1, end)

        # Find the optimized cost by reducing any price.
        max_reduced_cost = 0
        for i in range(n):
            max_reduced_cost = max(
                max_reduced_cost,
                dp(i, -1, True),
                dp(i, -1, False)
            )

        return total_cost - max_reduced_cost
