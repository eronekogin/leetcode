"""
https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
"""


class Solution:
    """
    Solution
    """

    def count_prefixes(self, words: list[str], s: str) -> int:
        """
        count prefixes
        """
        return sum(s.startswith(w) for w in words)
