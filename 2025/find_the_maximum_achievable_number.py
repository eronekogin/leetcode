"""
https://leetcode.com/problems/find-the-maximum-achievable-number/description/
"""


class Solution:
    """
    Solution
    """

    def the_maximum_achievable_x(self, num: int, t: int) -> int:
        """
        the maximum achievable x
        """
        return num + (t << 1)
