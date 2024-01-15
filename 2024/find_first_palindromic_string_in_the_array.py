"""
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
"""


class Solution:
    """
    Solution
    """

    def first_palindrome(self, words: list[str]) -> str:
        """
        first_palindrome
        """
        for w in words:
            if w == w[::-1]:
                return w

        return ''
