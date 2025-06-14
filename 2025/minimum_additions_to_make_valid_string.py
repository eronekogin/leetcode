"""
https://leetcode.com/problems/minimum-additions-to-make-valid-string/description/
"""


class Solution:
    """
    Solution
    """

    def add_minimum(self, word: str) -> int:
        """
        add minimum
        """
        occurrences = 0
        prev = 'z'
        for c in word:
            occurrences += c <= prev
            prev = c

        return occurrences * 3 - len(word)
