"""
https://leetcode.com/problems/total-hamming-distance/
"""


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        According to the question's statement, the numbers in the input list
        is less than 10^9, which is less than 2^30. So for
        each bit of the input number, if there are k numbers with that bit as 1
        while n - k numbers with that bit as 0, then they could form
        k * (n - k) pairs of difference for that bit, where n is the total
        length of the input list.
        """
        total, n = 0, len(nums)
        for currBit in range(31):
            currOnes = 0
            for num in nums:
                currOnes += (num >> currBit) & 1

            total += currOnes * (n - currOnes)

        return total

    def totalHammingDistance2(self, nums: List[int]) -> int:
        """
        Same idea as the above, but turning it into char group for each bit
        first:

        1. map('{:030b}'.format, nums) will return an iterator that turns each
            numbers in the input list to a 30 bits binary format string filled
            with leading zeros, for example:
                {:030b}'.format(100) = '000000000000000000000001100100'.

        2. *map will make each string as a parameter to the zip function.

        3. Then the zip function will take each char at the same position from
            each string and form a tuple, in other words, it will take all the
            bit at the same position from each number in the input list.
        """
        total = 0
        for b in zip(*map('{:030b}'.format, nums)):
            zeros = b.count('0')
            total += zeros * (len(b) - zeros)

        return total
