"""
https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
"""


from functools import cache


class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        @cache
        def dp(mask: int, i1: int):
            if i1 == N:
                return 0
            
            return min(
                dp(mask ^ (1 << i2), i1 + 1) + (nums1[i1] ^ nums2[i2])
                for i2 in range(N)
                if mask & (1 << i2)  # pick not used nums
            )

        N = len(nums1)
        return dp((1 << N) - 1, 0)
