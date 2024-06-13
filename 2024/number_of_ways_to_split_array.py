"""
https://leetcode.com/problems/number-of-ways-to-split-array/description/
"""


class Solution:
    """
    Solution
    """

    def ways_to_split_array(self, nums: list[int]) -> int:
        """
        ways to split array
        """
        total_sum, curr_sum = sum(nums), 0
        cnt = 0
        for i in range(len(nums) - 1):
            curr_sum += nums[i]
            if (curr_sum << 1) >= total_sum:
                cnt += 1

        return cnt
