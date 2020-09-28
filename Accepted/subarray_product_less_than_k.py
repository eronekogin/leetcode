"""
https://leetcode.com/problems/subarray-product-less-than-k/
"""


from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Presumption: the input list is not empty and all its elements are
        positive integers.
        """
        if k <= 1:
            return 0

        cnt, product, start = 0, 1, 0
        for end, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[start]
                start += 1

            cnt += end - start + 1

        return cnt
