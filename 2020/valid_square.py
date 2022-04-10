"""
https://leetcode.com/problems/valid-square/
"""


from typing import List


class Solution:
    def validSquare(
            self,
            p1: List[int],
            p2: List[int],
            p3: List[int],
            p4: List[int]) -> bool:
        def distance(p: List[int], q: List[int]) -> int:
            return (q[1] - p[1]) ** 2 + (q[0] - p[0]) ** 2

        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        d1, d2, d3, d4 = (distance(p1, p2), distance(p1, p3),
                          distance(p4, p2), distance(p4, p3))
        return d1 and d1 == d2 == d3 == d4 and \
            distance(p1, p4) == distance(p2, p3)
