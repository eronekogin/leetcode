"""
https://leetcode.com/problems/power-of-four/
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        1. num must be greater than zero.
        2. num must be a power of 2.
        3. for power of 4, the position of the only bit 1 should be in an odd
            position.
        """
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 == num
