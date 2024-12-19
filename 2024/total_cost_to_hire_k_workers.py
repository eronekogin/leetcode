"""
https://leetcode.com/problems/total-cost-to-hire-k-workers/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def total_cost(self, costs: list[int], k: int, candidates: int) -> int:
        """
        total cost
        """
        l, r = 0, len(costs) - 1
        h1: list[int] = []
        h2: list[int] = []
        cost = 0
        max_cost = max(costs) + 1

        while k:
            while len(h1) < candidates and l <= r:
                heappush(h1, costs[l])
                l += 1

            while len(h2) < candidates and l <= r:
                heappush(h2, costs[r])
                r -= 1

            c1 = h1[0] if h1 else max_cost
            c2 = h2[0] if h2 else max_cost

            if c1 <= c2:
                cost += c1
                heappop(h1)
            else:
                cost += c2
                heappop(h2)

            k -= 1

        return cost
