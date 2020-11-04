"""
https://leetcode.com/problems/consecutive-characters/
"""


class Solution:
    def maxPower(self, s: str) -> int:
        start, maxLen, = 0, 0
        for end, c in enumerate(s):
            if c != s[start]:
                maxLen = max(maxLen, end - start)
                start = end

        return max(maxLen, len(s) - start)
