"""
https://leetcode.com/problems/wildcard-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)
        restoreP, restoreS = None, None
        idxS, idxP = 0, 0

        while idxS < sLen:
            if idxP < pLen and p[idxP] in [s[idxS], '?']:
                # Same char or question mark is found, continue
                # to check the next char in s and p.
                idxS += 1
                idxP += 1
            elif idxP < pLen and p[idxP] == '*':
                # Star is found, save the current positions for later
                # restoration. Then scan the next char in p for matching.
                restoreP = idxP
                restoreS = idxS + 1
                idxP += 1
            elif restoreP is not None:
                # Not match is found, restore idxS and idxP to the previous
                # position to scan for the next possibility.
                idxS, idxP = restoreS, restoreP
            else:
                # Direct not match is found.
                return False

        # Check trailing stars. 'a*****' should still match 'a'.
        while idxP < pLen and p[idxP] == '*':
            idxP += 1

        # When coming here, s is already exhuasted, for p:
        # 1. p is not exhuasted, thus not match.
        # 2. p is exhuasted, so matched.
        return idxP == pLen


s = 'acdcb'
p = 'a*c?b'
print(Solution().isMatch(s, p))
