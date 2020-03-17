"""
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Traditional way is to divide 3 until the quotient == 1.
        Here for prime numbers, found the maximum power of 3 under 32 bits
        integer, which would be 3 ^ 19. (3^19 < 2^31 - 1 < 3^20). Then test
        if 3 ^ 19 could be divided by n.
        """
        return n > 0 and not 3 ** 19 % n
