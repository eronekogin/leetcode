"""
https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/description/
"""


class Solution:
    """
    Solution
    """

    def incremovable_subarray_count(self, nums: list[int]) -> int:
        """
        incremovable subarray count
        """
        n = len(nums)
        end = n - 1
        while end > 0 and nums[end - 1] < nums[end]:
            end -= 1

        if end == 0:
            # The original array is sorted, all subarray
            # from nums can be removed
            return n * (n + 1) // 2

        cnt = n - end + 1  # All prefix subarrays can be removed

        prev = 0
        for x in nums:
            if x <= prev:
                break

            prev = x

            # Move suffix to the right place
            while end < n and nums[end] <= x:
                end += 1

            # prefix + suffix can form a strictly sorted array
            # the middle ones can be removed
            cnt += n - end + 1

        return cnt
