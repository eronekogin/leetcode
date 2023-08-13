"""
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
"""

from string import ascii_lowercase


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        For any unique char from a to z, find the leftmost and rightmost occurrence of the char and count any
        unique char in the middle to form a aba palindrome.
        """
        cnt = 0
        for c in ascii_lowercase:
            l, r = s.find(c), s.rfind(c)
            if l > -1:
                cnt += len(set(s[l + 1: r]))
        
        return cnt
