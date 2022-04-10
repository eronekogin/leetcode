"""
https://leetcode.com/problems/single-number-iii/
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ab = 0  # Stores the xor of the two unique number.
        for num in nums:
            ab ^= num

        # Then get the rightmost bit where a and b is different.
        diff = ab & ~(ab - 1)

        # Partition the numbers into two groups which have this rightmost
        # bit set or not.
        a = 0
        for num in nums:
            if num & diff:
                a ^= num

        return [a, a ^ ab]  # a ^ (a ^ b) = b
