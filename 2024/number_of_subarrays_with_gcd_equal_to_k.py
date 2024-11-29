"""
https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/
"""


from math import gcd


class Solution:
    """
    Solution
    """

    def subarray_gcd(self, nums: list[int], k: int) -> int:
        """
        sub array gcd
        """
        cnt = 0
        for i, g in enumerate(nums):
            for j in range(i, len(nums)):
                g = gcd(g, nums[j])
                if g == k:
                    cnt += 1

                if g < k:
                    break

        return cnt
