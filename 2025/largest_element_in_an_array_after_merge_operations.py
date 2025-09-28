"""
https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/description/
"""


class Solution:
    """
    Solution
    """

    def max_array_value(self, nums: list[int]) -> int:
        """
        max array value
        """
        max_num = 0
        curr_num = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= curr_num:
                curr_num += nums[i]
            else:
                max_num = max(max_num, curr_num)
                curr_num = nums[i]

        return max(max_num, curr_num)


print(Solution().max_array_value(
    [5, 3, 3]))
