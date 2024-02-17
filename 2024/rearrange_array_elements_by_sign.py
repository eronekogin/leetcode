"""
https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
"""


class Solution:
    """
    Solution
    """

    def rearrange_array(self, nums: list[int]) -> list[int]:
        """
        rearrange_array
        """
        n = len(nums)
        rslt = [0] * n
        j = 0
        negative_nums: list[int] = []
        for x in nums:
            if x > 0:
                rslt[j] = x
                j += 2
            else:
                negative_nums.append(x)

        for j in range(1, len(nums), 2):
            rslt[j] = negative_nums[j >> 1]

        return rslt
