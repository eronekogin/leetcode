"""
https://leetcode.com/problems/non-overlapping-intervals/
"""


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        In order to get the minimum number of removed interval, it's best
        to keep the intervals that have the smaller end, because the smaller
        the interval's end is, the larger space it could provide for the
        other intervals to not overlap with itself.

        1. If the next interval is overlapping with the current one,
            simply discard it.
        2. If the next interval is not overlapping with the current one,
            take its end as the check for the next round.
        """
        end = float('-inf')
        removes = 0
        for iStart, iEnd in sorted(intervals, key=lambda x: x[1]):
            if iStart >= end:
                # The current interval is not overlapping with the previous
                # one. So take its end as the new previous end for next
                # round's checking.
                end = iEnd
            else:
                # The current interval is overlapping with the previous one.
                # So we simply discard it.
                removes += 1

        return removes
