"""
https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_sum(self, nums: list[int]) -> int:
        """
        maximum sum
        """
        return max(
            sum(
                nums[k * v * v - 1]
                for v in range(1, int((len(nums) // k) ** 0.5) + 1)
            )
            for k in range(1, len(nums) + 1)
        )
