"""
https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def remove_trailing_zeros(self, num: str) -> str:
        """
        remove trailing zeros
        """
        return num.rstrip('0')
