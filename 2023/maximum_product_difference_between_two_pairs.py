"""
https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
"""


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        sortedNums = sorted(nums)
        return sortedNums[-1] * sortedNums[-2] - sortedNums[0] * sortedNums[1]

        
