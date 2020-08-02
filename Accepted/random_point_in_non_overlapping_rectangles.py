"""
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
"""


from typing import List
from random import randint
from bisect import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        # Calculate the total number of points we could choose based on
        # the input rectangles.
        ranges, currSum = [0], 0
        for x1, y1, x2, y2 in rects:
            currSum += (x2 - x1 + 1) * (y2 - y1 + 1)
            ranges.append(currSum)

        self.ranges = ranges
        self.rects = rects

    def pick(self) -> List[int]:
        point = randint(0, self.ranges[-1] - 1)
        i = bisect(self.ranges, point)
        x1, y1, x2, y2 = self.rects[i - 1]  # Locate the start point.

        # Calculate the offset from the start point.
        offset = point - self.ranges[i - 1]

        # Then calculate where the target point is.
        # The total width of the current rectangle is x2 - x1 + 1,
        # so offset % width will give us the offset on the x axis and
        # offset // width will give us the offset on the y axis.
        dy, dx = divmod(offset, x2 - x1 + 1)
        return [x1 + dx, y1 + dy]


s = Solution([[1, 1, 5, 5]])
print(s.pick())
