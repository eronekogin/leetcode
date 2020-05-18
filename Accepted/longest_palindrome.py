"""
https://leetcode.com/problems/longest-palindrome/
"""


from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        rslt = hasSingleChar = 0
        for l in Counter(s).values():
            if l & 1:
                hasSingleChar = 1
                rslt += l - 1
            else:
                rslt += l

        if hasSingleChar:
            rslt += 1

        return rslt
