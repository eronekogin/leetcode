"""
https://leetcode.com/problems/generate-random-point-in-a-circle/
"""


from typing import List
from random import uniform


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xMin, self.xMax = x_center - radius, x_center + radius
        self.yMin, self.yMax = y_center - radius, y_center + radius
        self.r = radius
        self.x0 = x_center
        self.y0 = y_center

    def randPoint(self) -> List[float]:
        """
        Use reject sampling.
        """
        while True:
            x, y = uniform(self.xMin, self.xMax), uniform(self.yMin, self.yMax)
            if (x - self.x0) ** 2 + (y - self.y0) ** 2 <= self.r ** 2:
                return [x, y]


s = Solution(1.0, 0.0, 0.0)
print(s.randPoint())
