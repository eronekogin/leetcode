"""
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
"""


class Solution:
    def beautySum(self, s: str) -> int:
        rslt = 0
        base = ord('a')
        for start in range(len(s)):
            freqs = [0] * 26
            for end in range(start, len(s)):
                freqs[ord(s[end]) - base] += 1
                rslt += max(freqs) - min(x for x in freqs if x > 0)

        return rslt
