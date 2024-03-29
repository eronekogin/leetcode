"""
https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
"""


from math import sqrt


class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        # a sub function that calculates the center of the circle
        def circles_from_p1p2r(p1, p2, r):
            (x1, y1), (x2, y2) = p1, p2

            # delta x, delta y between darts
            dx, dy = x2 - x1, y2 - y1

            # dist between darts
            q = sqrt(dx**2 + dy**2)

            # if two darts are too far away, there is no such circle
            if q > 2.0*r:
                return []

            # find the halfway point
            x3, y3 = (x1+x2)/2, (y1+y2)/2

            # distance along the mirror line
            d = sqrt(r**2-(q/2)**2)

            # One circle
            c1 = [x3 - d*dy/q, y3 + d*dx/q]

            # The other circle
            c2 = [x3 + d*dy/q, y3 - d*dx/q]
            return [c1, c2]

        # now the main function
        res = 0
        n = len(darts)

        for p in range(n):
            for q in range(p+1, n):

                # Find the two candidate circle for each pair of darts
                TwoCirs = circles_from_p1p2r(darts[p], darts[q], r)

                # count how many dots are inside the circle
                for center in TwoCirs:  # center = TwoCirs[1]
                    cnt = 0

                    for dots in darts:  # dots =darts[0]
                        if (dots[0]-center[0])**2 + (dots[1]-center[1])**2 <= r**2+10**-6:
                            cnt += 1
                    res = max(res, cnt)

        return res if res else 1
