"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        The question equals to find the total number of the minimum
        overlapped intervals.
        """
        arrows, maxEnd = 0, float('-inf')
        for x1, x2 in sorted(points, key=lambda x: x[1]):
            if x1 > maxEnd:
                maxEnd = x2
                arrows += 1

        return arrows
