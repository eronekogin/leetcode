"""
https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/description/
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

        if end == 0:  # the list is sorted
            return n * (n + 1) // 2

        cnt = n - end + 1  # All prefix can be safely removed

        prev = 0
        for x in nums:
            if x <= prev:
                break

            prev = x

            while end < n and nums[end] <= x:
                end += 1

            cnt += n - end + 1  # any suffix can append to the current prefix

        return cnt
