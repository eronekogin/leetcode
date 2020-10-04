"""
https://leetcode.com/problems/remove-covered-intervals/
"""


from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        cnt, end = 0, float('-inf')
        sortedIntervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        for _, e in sortedIntervals:
            if e > end:
                cnt += 1

            end = max(end, e)

        return cnt


print(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
