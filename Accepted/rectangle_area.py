"""
https://leetcode.com/problems/rectangle-area/
"""


class Solution:
    def computeArea(
            self, A: int, B: int, C: int, D: int,
            E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (H - F) * (G - E)
        areaOverlap =\
            self.calc_overlap(A, C, E, G) * self.calc_overlap(B, D, F, H)
        return area1 + area2 - areaOverlap

    def calc_overlap(self, l1: int, r1: int, l2: int, r2: int) -> int:
        if r1 < l2 or r2 < l1:
            return 0  # No overlap.

        return min(r1, r2) - max(l1, l2)
