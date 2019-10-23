"""
https://leetcode.com/problems/single-number/
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Use exclusive or action on each number in the nums. Since
        a ^ b ^ a = a ^ a ^ b = 0 ^ b = b, after walking through all
        the number we will get the only number that occurs once.
        """
        rslt = 0
        for num in nums:
            rslt ^= num

        return rslt
