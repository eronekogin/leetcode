"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""


from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1)

        # Must contain same types of chars.
        if set(str1) != set(str2):
            return ''

        # Find the value of t.
        maxLen = gcd(len(str1), len(str2))
        t = str1[:maxLen]

        # Validate strings.
        if any(t * (len(s) // maxLen) != s for s in [str1, str2]):
            return ''

        return t
