"""
https://leetcode.com/problems/apply-operations-to-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def apply_operations(self, nums: list[int]) -> list[int]:
        """
        apply operations
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] <<= 1
                nums[i + 1] = 0

        rslt: list[int] = []
        zeros = 0
        for x in nums:
            if x == 0:
                zeros += 1
            else:
                rslt.append(x)

        return rslt + [0] * zeros
