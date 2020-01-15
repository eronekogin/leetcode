"""
https://leetcode.com/problems/shortest-palindrome/
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Try to find the longest palindrome staring at the front of s.
        Then append the reverse of the remaining s to the front of s
        as the result.
        An example is as follows:

        s          dedcba
        r[0:]      abcded    Nope...
        r[1:]   (a)bcded     Nope...
        r[2:]  (ab)cded      Nope...
        r[3:] (abc)ded       Yes! Return abc + dedcba
        """
        if not s:  # s is an empty string.
            return s

        r, n = s[::-1], len(s)
        for i in range(n):
            # The str.startswith() method is written in c, which is
            # reducing the time cost of this brutal force algorithm.
            if s.startswith(r[i:]):
                return r[:i] + s
