"""
https://leetcode.com/problems/di-string-match/
"""


class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        l, r = 0, len(s)
        rslt = []
        for c in s:
            if c == 'I':
                rslt.append(l)
                l += 1
            else:
                rslt.append(r)
                r -= 1

        # Add the last number as now l must be equal to r.
        rslt.append(l)

        return rslt
