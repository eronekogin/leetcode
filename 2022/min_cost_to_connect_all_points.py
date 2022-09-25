"""
https://leetcode.com/problems/min-cost-to-connect-all-points/
"""


from heapq import heappush, heappop


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def get_distance(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        rslt = 0
        N = len(points)
        visited: set[int] = set()
        nodes: list[tuple[int]] = [(0, 0, 0)]

        while len(visited) < N:
            minDistance, _, currNode = heappop(nodes)
            if currNode in visited:
                continue

            rslt += minDistance
            visited.add(currNode)

            for nextNode in range(N):
                if nextNode not in visited:
                    heappush(
                        nodes,
                        (
                            get_distance(*points[currNode], *points[nextNode]),
                            currNode,
                            nextNode
                        )
                    )

        return rslt
