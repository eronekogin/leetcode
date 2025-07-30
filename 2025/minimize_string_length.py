"""
https://leetcode.com/problems/minimize-string-length/description/
"""


class Solution:
    """
    Solution
    """

    def minimized_string_length(self, s: str) -> int:
        """
        minimized string length
        """
        return len(set(s))
