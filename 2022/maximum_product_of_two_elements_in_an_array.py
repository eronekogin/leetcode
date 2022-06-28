"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        sortedNums = sorted(nums)
        return (sortedNums[-1] - 1) * (sortedNums[-2] - 1)
