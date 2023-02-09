"""
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
"""


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        """
        abs of subarray sum = one prefix sum - another prefix sum
            <= max prefix sum - min prefix sum
        """
        preSums = [0]
        for num in nums:
            preSums.append(preSums[-1] + num)

        return max(preSums) - min(preSums)


print(Solution().maxAbsoluteSum([-1]))
