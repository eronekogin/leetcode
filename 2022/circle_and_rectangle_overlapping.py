"""
https://leetcode.com/problems/circle-and-rectangle-overlapping/
"""


class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int
    ) -> bool:
        """
        1. Get the closest point to the circle on the rectangle
        2. If the distance of this point to the center of the round is no
            more than the radius, it means the point is inside the round.
        """
        def get_closest_val(currVal: int, minVal: int, maxVal: int) -> int:
            return max(minVal, min(currVal, maxVal))

        x = get_closest_val(xCenter, x1, x2)
        y = get_closest_val(yCenter, y1, y2)
        dx = x - xCenter
        dy = y - yCenter

        return dx * dx + dy * dy <= radius * radius
