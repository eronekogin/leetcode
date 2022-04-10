"""
https://leetcode.com/problems/sum-of-two-integers/
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Python has unlimited size of integer so here we have to
        get just the lower 32 bits of the target integer in order
        to terminate the loop when it reaches the 32 bits limit.
        """
        MAX_32_INT = 0x7FFFFFFF
        MASK_32_BITS = 0xFFFFFFFF
        totalSum, num = a, b
        while num:
            # Carry only happens when both totalSum and num has 1
            # in the same bit position.
            carry = totalSum & num

            # totalSum ^ num adds any bits together when they are
            # not the same. For the same ones it will be reduced to zero.
            totalSum = (totalSum ^ num) & MASK_32_BITS

            # When carry happens, it will be carried to
            # its totalSum adjancent bit.
            # So we give it to num for the next round of add.
            num = (carry << 1) & MASK_32_BITS

        if totalSum > MAX_32_INT:
            totalSum ^= ~MASK_32_BITS

        return totalSum


print(Solution().getSum(-1, 1))
