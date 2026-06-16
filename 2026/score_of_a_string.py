"""
https://leetcode.com/problems/score-of-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def score_of_string(self, s: str) -> int:
        """
        score of string
        """
        return sum(
            abs(ord(a) - ord(b))
            for a, b in zip(s, s[1:])
        )
