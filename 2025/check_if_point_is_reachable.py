"""
https://leetcode.com/problems/check-if-point-is-reachable/description/
"""


from math import gcd


class Solution:
    """
    Solution
    """

    def is_reachable(self, target_x: int, target_y: int) -> bool:
        """
        gcd(x, y) must be 2^k, otherwise from point (x, y) we
        cannot go back to (1, 1)
        """
        return gcd(target_x, target_y).bit_count() == 1
