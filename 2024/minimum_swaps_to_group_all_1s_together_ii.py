"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/
"""


class Solution:
    """
    Solution
    """

    def min_swaps(self, nums: list[int]) -> int:
        """
        min_swaps
        """
        if len(nums) <= 1:
            return 0

        total_ones = nums.count(1)
        concat_nums = nums + nums

        start = zero_cnt = 0
        min_swaps = len(nums)
        for end, num in enumerate(concat_nums):
            if end >= total_ones:
                min_swaps = min(min_swaps, zero_cnt)
                zero_cnt -= concat_nums[start] == 0
                start += 1

            zero_cnt += num == 0

        return min_swaps
