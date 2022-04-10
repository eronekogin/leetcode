"""
https://leetcode.com/problems/next-greater-element-i/
"""


from typing import List


class Solution:
    def nextGreaterElement(
            self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {v: i for i, v in enumerate(nums2)}
        n = len(nums2)
        rslt = [None] * len(nums1)
        for i1, v in enumerate(nums1):
            i2 = memo[v] + 1
            while i2 < n and v >= nums2[i2]:
                i2 += 1

            if i2 == n:
                rslt[i1] = -1
            else:
                rslt[i1] = nums2[i2]

        return rslt
