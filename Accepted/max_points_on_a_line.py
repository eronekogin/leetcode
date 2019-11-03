"""
https://leetcode.com/problems/max-points-on-a-line/
"""


from typing import List, Tuple


class Solution:
    def _gcd(self, x: int, y: int) -> int:
        """
        Use Euclid's algorithm to calculate the greatest common divisor of 
        x and y. The algorithm is based on the theorem as follows:
        gcd(x, y) == gcd(y, x % y).
        """
        a, b, r = x, y, 0
        while b:
            r = a % b
            a = b
            b = r

        return a

    def _frac(self, x: int, y: int) -> Tuple[int, int]:
        g = self._gcd(x, y)
        return (x // g, y // g)

    def maxPoints(self, points: List[List[int]]) -> int:
        n, currMax = len(points), 0
        for i in range(n):
            xi, yi = points[i]
            memo = {'v': 1}
            samePointCnt = 0
            for j in range(i + 1, n):
                xj, yj = points[j]
                if points[i] == points[j]:  # Same point.
                    samePointCnt += 1
                elif xj == xi:  # Verticle.
                    memo['v'] += 1
                else:
                    """
                    We can't simple calculate the slope as dy / dx
                    as the precision of the result is not sufficient.
                    So we use fraction format instead.
                    """
                    slope = self._frac((yj - yi), (xj - xi))
                    memo[slope] = memo.get(slope, 1) + 1

            currMax = max(currMax, max(memo.values()) + samePointCnt)

        return currMax


print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))
