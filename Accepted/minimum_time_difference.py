"""
https://leetcode.com/problems/minimum-time-difference/
"""


from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        sortedMinutes = sorted(
            int(x[:2]) * 60 + int(x[3:]) for x in timePoints)
        sortedMinutes.append(sortedMinutes[0] + 24 * 60)
        return min(
            sortedMinutes[i + 1] - sortedMinutes[i]
            for i in range(len(sortedMinutes) - 1))
