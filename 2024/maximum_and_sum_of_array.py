"""
https://leetcode.com/problems/maximum-and-sum-of-array/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def maximum_and_sum(self, nums: list[int], num_slots: int) -> int:
        """
        Each slot can contain at most two numbers, so we use base-3 to generate
        a mask for each slot's available spots.

        For example, suppose we have five slots, all filled with 2 numbers, then
        our mask will be 22222.

        Then if we remove 1 number from the 3rd slot, it will become 22122, and
        if we remove all numbers from the 3rd slot, it will become 22022, such
        case is like 22222 - 3 ** 2 to remove one number.
        """
        @cache
        def dp(i: int, mask: int):
            if i == len(nums):
                return 0

            max_sum = 0
            for slot in range(1, num_slots + 1):
                offset = 3 ** (slot - 1)
                if (mask // offset) % 3 > 0:  # current slot still has spot to use
                    max_sum = max(
                        max_sum,
                        (nums[i] & slot) + dp(i + 1, mask - offset)
                    )

            return max_sum

        return dp(0, 3 ** num_slots - 1)
