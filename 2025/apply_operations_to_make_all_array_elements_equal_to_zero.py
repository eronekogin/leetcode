"""
https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/description/
"""


class Solution:
    """
    Solution
    """

    def check_array(self, nums: list[int], k: int) -> bool:
        """
        check array
        """
        if k <= 1 or len(nums) <= 1:
            return True

        curr_sum = 0
        for i, x in enumerate(nums):
            if curr_sum > x:
                return False

            nums[i], curr_sum = x - curr_sum, x

            if i >= k - 1:
                curr_sum -= nums[i - k + 1]

        return curr_sum == 0
