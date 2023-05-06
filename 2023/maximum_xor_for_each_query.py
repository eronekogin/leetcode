"""
https://leetcode.com/problems/maximum-xor-for-each-query/
"""


from functools import reduce


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        currXor = reduce(lambda acc, curr: acc ^ curr, nums)
        mask = (1 << maximumBit) - 1
        rslt: list[int] = []
        for num in reversed(nums):
            maxNum = currXor | mask
            rslt.append(currXor ^ maxNum)
            currXor ^= num

        return rslt
