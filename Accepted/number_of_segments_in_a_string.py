"""
https://leetcode.com/problems/number-of-segments-in-a-string/
"""


class Solution:
    def countSegments(self, s: str) -> int:
        segments, preC = 0, ' '
        for c in s:
            if c == ' ' and preC != ' ':
                segments += 1

            preC = c

        if preC != ' ':
            segments += 1

        return segments


print(Solution().countSegments("Hello, my name is John"))
