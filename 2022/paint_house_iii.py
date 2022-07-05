"""
https://leetcode.com/problems/paint-house-iii/
"""


from functools import lru_cache


class Solution:
    def minCost(
        self,
        houses: list[int],
        cost: list[list[int]],
        m: int,
        n: int,
        target: int
    ) -> int:
        @lru_cache(None)
        def dfs(
            currHouse: int,
            prevColor: int,
            remainingNeighbors: int
        ) -> int:
            if remainingNeighbors < 0 or m - currHouse < remainingNeighbors:
                # Too many neigbours or not enough house to visit.
                return float('inf')

            if currHouse == m:  # visited all houses.
                if remainingNeighbors == 0:
                    return 0
                else:
                    return float('inf')

            if houses[currHouse] == 0:  # Current house not painted.
                return min(
                    cost[currHouse][color - 1] + dfs(
                        currHouse + 1,
                        color,
                        remainingNeighbors - (color != prevColor)
                    )
                    for color in range(1, n + 1)
                )
            else:
                return dfs(
                    currHouse + 1,
                    houses[currHouse],
                    remainingNeighbors - (houses[currHouse] != prevColor)
                )

        minCost = dfs(0, -1, target)
        if minCost == float('inf'):
            return -1  # Not possible.

        return minCost
