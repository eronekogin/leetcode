"""
https://leetcode.com/problems/power-of-two/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Power of 2 means the binary form of n only contains 1 bit of 1,
        and the remaining bits are zeros.
        """
        if n < 1:
            return False

        return not (n & (n - 1))  # 1000 & 0111 = 0000 = 0
