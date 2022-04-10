"""
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        The possible center of each palindrome sub string is either at each
        char of s or between each char of s. So we could try to check each
        center poistion and expand the palindrome to its longest length.
        """
        cnt, n = 0, len(s)
        for center in range((n << 1) - 1):
            l = center >> 1
            r = l + (center & 1)
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

        return cnt
