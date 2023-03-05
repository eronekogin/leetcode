"""
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
"""


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        minDistance = float('inf')
        minIndex = -1
        for i, [x1, y1] in enumerate(points):
            if x1 == x or y1 == y:
                if abs(x1 - x) + abs(y1 - y) < minDistance:
                    minIndex = i
                    minDistance = abs(x1 - x) + abs(y1 - y)

        return minIndex
