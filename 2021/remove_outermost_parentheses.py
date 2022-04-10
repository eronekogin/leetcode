"""
https://leetcode.com/problems/remove-outermost-parentheses/
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l = lCnt = rCnt = 0
        rslt = []
        for r, c in enumerate(s):
            if c == '(':
                lCnt += 1
            else:
                rCnt += 1

            if lCnt == rCnt:
                rslt.append(s[l + 1: r])
                l = r + 1
                lCnt = rCnt = 0

        return ''.join(rslt)
