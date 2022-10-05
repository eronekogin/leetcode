"""
https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/
"""


from functools import cache


class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        @cache
        def dp(r: int, mask: int) -> int:
            if r == R:
                # When all points in group 1 are connected, find any point
                # in group 2 that are not connnected yet, and connnect them
                # to the points in group 1 with minimum cost.
                costCnt = 0
                for c in range(C):
                    if not mask & (1 << c):
                        costCnt += minCostForGroup2PointsToConnect[c]

                return costCnt

            # Otherwise, connect each point from group 1 first to group 2
            # points with one edge for each point.
            costCnt = float('inf')
            for c in range(C):
                costCnt = min(
                    costCnt,
                    cost[r][c] + dp(r + 1, mask | (1 << c))
                )

            return costCnt

        R, C = len(cost), len(cost[0])

        # Initialize the minimum cost list for the points in group 2 to
        # connect to points in group 1.
        minCostForGroup2PointsToConnect = [min(x) for x in zip(*cost)]

        # Calculate result.
        return dp(0, 0)
