"""
https://leetcode.com/problems/product-of-array-except-self/
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rslt = [1] * n

        # Product from left, through top to bottom.
        for i in range(1, n):
            rslt[i] = rslt[i - 1] * nums[i - 1]

        # Product from right, through bottom to top.
        r = 1
        for i in reversed(range(n)):
            rslt[i] *= r
            r *= nums[i]

        return rslt
