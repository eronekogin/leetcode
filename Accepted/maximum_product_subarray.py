"""
https://leetcode.com/problems/maximum-product-subarray/
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Using dymanic planning solution. dp[i] contains the mininum and the
        maximum product produced by the nums[:i].
        """
        if not nums:
            return 0

        maxP = preMaxP = preMinP = nums[0]
        for num in nums[1:]:
            preMinP, _, preMaxP = sorted([num, preMaxP * num, preMinP * num])
            maxP = max(maxP, preMaxP)

        return maxP


nums = [-5, 0, 2]
print(Solution().maxProduct(nums))
