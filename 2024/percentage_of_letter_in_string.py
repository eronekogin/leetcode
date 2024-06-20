"""
https://leetcode.com/problems/percentage-of-letter-in-string/description/
"""


class Solution:
    """
    Solution
    """

    def percentage_letter(self, s: str, letter: str) -> int:
        """
        percentage letter
        """
        return s.count(letter) * 100 // len(s)
