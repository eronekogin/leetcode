"""
https://leetcode.com/problems/1-bit-and-2-bit-characters/
"""


from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        Keep track of the start index of the next character:
        1. If the current char is 0, the next char must take 1 bit.
        2. If the current char is 1, the next char must take 2 bits.

        Then if the last char start at the last index of bits, it must be a
        single bit char.
        """
        start, N = 0, len(bits) - 1
        while start < N:
            start += bits[start] + 1

        return start == N
