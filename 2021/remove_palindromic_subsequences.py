"""
https://leetcode.com/problems/remove-palindromic-subsequences/
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:  # s is empty.
            return 0

        if s[::-1] == s:  # s is already a palindrome.
            return 1

        return 2  # Remove all a in s, then remove the remaining.
