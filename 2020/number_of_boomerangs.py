"""
https://leetcode.com/problems/number-of-boomerangs/
"""


from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        rslt = 0
        for x0, x1 in points:
            memo = defaultdict(int)  # distance: number of points.
            for y0, y1 in points:
                # Calculate the distance from x to each point.
                d = (y0 - x0) ** 2 + (y1 - x1) ** 2

                # If the distance is existing, the current point could
                # form new pairs with the previous points.
                rslt += memo[d] << 1

                # Increase the total number of points
                memo[d] += 1

        return rslt
