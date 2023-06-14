"""
https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxOnes = maxZeros = 0
        start = 0
        for end, c in enumerate(s):
            if c != s[start]:
                if c == '0':
                    maxOnes = max(maxOnes, end - start)
                else:
                    maxZeros = max(maxZeros, end - start)

                start = end

        if s[-1] == '0':
            maxZeros = max(maxZeros, len(s) - start)
        else:
            maxOnes = max(maxOnes, len(s) - start)

        return maxOnes > maxZeros


print(Solution().checkZeroOnes('1101'))
