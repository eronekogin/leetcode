"""
https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/
"""

from collections import Counter


class Solution:
    """
    Solution
    """

    def check_strings(self, s1: str, s2: str) -> bool:
        """
        check strings
        """
        return (
            Counter(s1[0::2]) == Counter(s2[0::2]) and
            Counter(s1[1::2]) == Counter(s2[1::2])
        )
