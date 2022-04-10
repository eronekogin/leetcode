"""
https://leetcode.com/problems/interval-list-intersections/
"""


from typing import List


class Solution:
    def intervalIntersection(
            self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        na, nb = len(A), len(B)
        rslt = []
        ia = ib = 0
        while ia < na and ib < nb:
            sa, ea = A[ia]
            sb, eb = B[ib]
            sr = max(sa, sb)
            er = min(ea, eb)
            if sr <= er:
                rslt.append((sr, er))

            if ea < eb:
                ia += 1
            else:
                ib += 1

        return rslt
