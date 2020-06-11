"""
https://leetcode.com/problems/find-right-interval/
"""


from typing import List
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        Presumptions:

        1. The start of each interval is unique.
        2. For each interval, the end > the start.

        Sort the intervals by the unique start points, then search each end
        point in the sorted list to find the minimum start point that is
        greater or equal to the current end point.
        """
        starts = [(x[0], i) for i, x in enumerate(intervals)]
        starts.sort()
        starts += [(float('inf'), -1)]
        return [starts[bisect_left(starts, (x[1], -1))][1] for x in intervals]
