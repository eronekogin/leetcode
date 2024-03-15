"""
https://leetcode.com/problems/counting-words-with-a-given-prefix/description/
"""


class Solution:
    """
    Solution
    """

    def prefix_count(self, words: list[str], pref: str) -> int:
        """
        prefix count
        """
        return sum(w.startswith(pref) for w in words)
