"""
https://leetcode.com/problems/can-convert-string-in-k-moves/
"""


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        memo = [0] * 26
        for a, b in zip(s, t):
            needShifts = (ord(b) - ord(a)) % 26
            if needShifts > 0 and memo[needShifts] * 26 + needShifts > k:
                # When the same shifts occurs again, need to make more moves
                # in order to achieve the same goal.
                return False

            memo[needShifts] += 1

        return True
