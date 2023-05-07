"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/
"""


class Solution:
    def makeStringSorted(self, s: str) -> int:
        cnt = [0] * 26
        rslt = 0
        charsOnward = 0
        combCharsOnWard = 1
        offset = ord('a')
        for c in reversed(s):
            i = ord(c) - offset
            cnt[i] += 1
            charsOnward += 1
            combCharsOnWard = combCharsOnWard * charsOnward // cnt[i]
            rslt += combCharsOnWard * sum(cnt[:i]) // charsOnward

        return rslt % (10 ** 9 + 7)
