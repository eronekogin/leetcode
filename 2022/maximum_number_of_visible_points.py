"""
https://leetcode.com/problems/maximum-number-of-visible-points/
"""


from math import pi, atan2


class Solution:
    def visiblePoints(
        self,
        points: list[list[int]],
        angle: int,
        location: list[int]
    ) -> int:
        """
        See https://www.grc.nasa.gov/www/k-12/airplane/Images/coords.jpg
        for the explanation on arctan, the the remaining is basically a
        sliding window solution.
        """
        targetAngles: list[float] = []
        x0, y0 = location
        extraPoints = 0

        for x, y in points:
            if x == x0 and y == y0:
                extraPoints += 1
            else:
                targetAngles.append(atan2(y - y0, x - x0))

        targetAngles.sort()
        targetAngles.extend([x + 2 * pi for x in targetAngles])
        angle0 = pi * angle / 180

        l = cnt = 0
        for r in range(len(targetAngles)):
            while targetAngles[r] - targetAngles[l] > angle0:
                l += 1

            cnt = max(cnt, r - l + 1)

        return cnt + extraPoints
