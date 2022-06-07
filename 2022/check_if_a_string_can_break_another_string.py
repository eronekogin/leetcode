"""
https://leetcode.com/problems/check-if-a-string-can-break-another-string/
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ss1, ss2 = sorted(s1), sorted(s2)
        return (
            all(c1 >= c2 for c1, c2 in zip(ss1, ss2)) or
            all(c1 <= c2 for c1, c2 in zip(ss1, ss2))
        )
