"""
https://leetcode.com/problems/insert-interval/
"""

from typing import List


class Solution:
    def insert(
            self,
            intervals: List[List[int]],
            newInterval: List[int]) -> List[List[int]]:
        # The input intervals are assumed to be sorted by the first value
        # before passed to this function.
        before, after = [], []
        newMin, newMax = newInterval
        for interval in intervals:
            if interval[0] > newInterval[1]:
                after.append(interval)
            elif interval[1] < newInterval[0]:
                before.append(interval)
            else:
                newMin = min(newMin, interval[0])
                newMax = max(newMax, interval[1])

        return before + [[newMin, newMax]] + after


intervals = [[1, 5], [6, 8]]
newInterval = [5, 6]
print(Solution().insert(intervals, newInterval))
