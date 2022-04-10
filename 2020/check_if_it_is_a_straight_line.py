"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""


from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates:
            return False

        n = len(coordinates)
        if n <= 2:
            return True

        x0, y0 = coordinates[0]
        dx, dy = coordinates[1][0] - x0, coordinates[1][1] - y0
        for i in range(2, n):
            x, y = coordinates[i]
            if (x - x0) * dy != (y - y0) * dx:
                return False

        return True
