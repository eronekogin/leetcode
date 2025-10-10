"""
https://leetcode.com/problems/check-if-it-is-possible-to-split-array/description/
"""


class Solution:
    """
    Solution
    """

    def can_split_array(self, nums: list[int], m: int) -> bool:
        """
        if we found any pair (nums[i], nums[i + 1]) having their
        sum >= m, we can split other items in nums to size one array
        until this pair. then we split this pair to two size one arrays
        """
        if len(nums) <= 2:
            return True

        return any(
            a + b >= m
            for a, b in zip(nums, nums[1:])
        )


print(Solution().can_split_array([2, 3, 3, 2, 3], 6))
