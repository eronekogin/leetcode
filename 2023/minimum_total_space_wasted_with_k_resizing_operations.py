"""
https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/
"""


from functools import cache


class Solution:
    def minSpaceWastedKResizing(self, nums: list[int], k: int) -> int:
        @cache
        def dp(i: int, k: int):
            """
            Suppose dp[i][k] stands for the minumum waste space by resizing k times in nums[i..N].
            """
            if i == N:
                return 0
            
            if k == -1:
                return MAX_WASTE_SPACE

            rslt = MAX_WASTE_SPACE
            maxElements = nums[i]
            totalSum = 0

            for j in range(i, N):
                maxElements = max(maxElements, nums[j])
                totalSum += nums[j]
                wasted = maxElements * (j - i + 1) - totalSum
                rslt = min(rslt, dp(j + 1, k - 1) + wasted)
            
            return rslt


        N = len(nums)
        MAX_WASTE_SPACE = 200 * 10 ** 6
        return dp(0, k)
