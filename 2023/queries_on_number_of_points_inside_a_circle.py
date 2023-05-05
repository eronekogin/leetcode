"""
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""


class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        rslt = []
        for x0, y0, r in queries:
            cnt = 0
            maxDistance = r * r
            for x, y in points:
                if (x - x0) ** 2 + (y - y0) ** 2 <= maxDistance:
                    cnt += 1

            rslt.append(cnt)

        return rslt
