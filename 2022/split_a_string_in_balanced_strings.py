"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = splits = 0
        for c in s:
            if c == 'L':
                balance += 1
            else:
                balance -= 1

            if not balance:
                splits += 1

        return splits
