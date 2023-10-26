"""
https://leetcode.com/problems/detect-squares/
"""


from collections import Counter, defaultdict


class DetectSquares:
    """
    DetectSquares
    """

    def __init__(self):
        self.points_cnt = Counter()
        self.x_points = defaultdict(Counter)

    def add(self, point: list[int]) -> None:
        """
        add a new point
        """
        x, y = point
        self.points_cnt[(x, y)] += 1
        self.x_points[x][y] += 1

    def count(self, point: list[int]) -> int:
        """
        count square.
        """
        x0, y0 = point
        cnt = 0

        # Search y axis.
        for y in self.x_points[x0]:
            if y != y0:
                size = y - y0
                cnt += (
                    self.points_cnt[(x0, y)] *
                    self.points_cnt[(x0 + size, y)] *
                    self.points_cnt[(x0 + size, y0)]
                ) + (
                    self.points_cnt[(x0, y)] *
                    self.points_cnt[(x0 - size, y)] *
                    self.points_cnt[(x0 - size, y0)]
                )

        return cnt
