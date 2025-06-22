"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/
"""


from math import gcd


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int]) -> int:
        """
        min operations
        """
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        min_subarray_len = n + 1
        for start, g in enumerate(nums):
            for end in range(start + 1, n):
                g = gcd(g, nums[end])
                if g == 1:
                    min_subarray_len = min(
                        min_subarray_len,
                        end - start
                    )
                    break

        if min_subarray_len == n + 1:
            return -1  # cannot convert

        # If minimum subarray can be found, we can
        # perform the action from the end of the subarray
        # to the start to make nums[start] to 1, then use
        # this one to convert the remaining n - 1 numbers
        return min_subarray_len + n - 1
