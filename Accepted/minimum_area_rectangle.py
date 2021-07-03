"""
https://leetcode.com/problems/minimum-area-rectangle/
"""


from collections import defaultdict
from itertools import combinations


class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        minArea = float('inf')
        visited = set()
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    # Found a rectangle now.
                    minArea = min(minArea, abs(y1 - y2) * abs(x1 - x2))

            visited.add((x1, y1))

        if minArea == float('inf'):
            return 0  # No rectangle has been found.

        return minArea

    def minAreaRect2(self, points: list[list[int]]) -> int:
        N = len(points)
        nx = len({x for x, _ in points})
        ny = len({y for _, y in points})

        if nx == N or ny == N:
            # All x or all y are different, which means they cannot form any
            # rectangle.
            return 0

        memo = defaultdict(list)
        if nx > ny:
            for x, y in points:
                memo[x].append(y)
        else:
            for x, y in points:
                memo[y].append(x)

        # Sort the axis which has less points, then scan on the other axis.
        visited = {}
        minArea = float('inf')
        for x in sorted(memo):
            memo[x].sort()
            for y1, y2 in combinations(memo[x], 2):
                if (y1, y2) in visited:
                    minArea = min(minArea, (x - visited[(y1, y2)]) * (y2 - y1))

                visited[(y1, y2)] = x

        if minArea == float('inf'):
            return 0  # No rectangle has been found.

        return minArea
