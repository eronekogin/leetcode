"""
https://leetcode.com/problems/minimum-time-visiting-all-points/
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        px, py = points[0]
        stepCnt = 0
        for x, y in points[1:]:
            stepCnt += max(abs(x - px), abs(y - py))
            px, py = x, y

        return stepCnt


print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
