"""
https://leetcode.com/problems/merge-intervals/
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the invervals by its left value in ascending order.
        rslt = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if rslt and rslt[-1][1] >= interval[0]:  # Has overlap.
                rslt[-1][1] = max(rslt[-1][1], interval[1])
            else:  # No overlap.
                rslt.append(interval)

        return rslt


intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
print(Solution().merge(intervals))
