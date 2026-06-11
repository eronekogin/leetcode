"""
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
"""


class Solution:
    """
    Solution
    """

    def longest_monotonic_subarray(self, nums: list[int]) -> int:
        """
        longest monotnoic subarray
        """
        increase_len = decrease_len = max_len = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                increase_len += 1
                decrease_len = 1
            elif nums[i + 1] < nums[i]:
                increase_len = 1
                decrease_len += 1
            else:
                increase_len = decrease_len = 1

            max_len = max(
                max_len,
                increase_len,
                decrease_len
            )

        return max_len


print(Solution().longest_monotonic_subarray([1, 4, 3, 3, 2]))
