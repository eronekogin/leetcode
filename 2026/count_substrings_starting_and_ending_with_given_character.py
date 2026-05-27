"""
https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/description/
"""


class Solution:
    """
    Solution
    """

    def count_substrings(self, s: str, c: str) -> int:
        """
        count substrings
        """
        total = s.count(c)
        return (1 + total) * total // 2
