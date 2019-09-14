"""
https://leetcode.com/problems/decode-ways/
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        preCuts, currCuts, preDigit = 0, int(s > ''), ''
        for currDigit in s:
            nextCuts = (currDigit > '0') * currCuts + (
                9 < int(preDigit + currDigit) < 27) * preCuts
            preCuts, preDigit = currCuts, currDigit
            currCuts = nextCuts

        return currCuts


print(Solution().numDecodings('1020'))
