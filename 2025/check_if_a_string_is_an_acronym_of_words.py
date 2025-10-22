"""
https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
"""


class Solution:
    """
    Solution
    """

    def is_acronym(self, words: list[str], s: str) -> bool:
        """
        is acronym
        """
        return ''.join(w[0] for w in words) == s
