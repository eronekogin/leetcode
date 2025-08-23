"""
https://leetcode.com/problems/construct-the-longest-new-string/description/
"""


class Solution:
    """
    Solution
    """

    def longest_string(self, x: int, y: int, z: int) -> int:
        """
        longest string
        """
        return min(x, y) * 4 + z * 2 + 2 * (x != y)
