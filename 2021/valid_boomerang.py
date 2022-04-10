"""
https://leetcode.com/problems/valid-boomerang/
"""


from itertools import combinations


class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        if len({tuple(p) for p in points}) != len(points):  # Has duplicates.
            return False

        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            if x1 == x2:
                if x2 == x3:
                    return False  # On the same line.
            else:
                if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
                    return False  # On the same line.

        return True
