"""
https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/description/
"""


class Solution:
    """
    Solution
    """

    def longest_alternating_subarray(self, nums: list[int], threshold: int) -> int:
        """
        longest alternating subarray
        """
        l = 0
        max_len = 0
        n = len(nums)
        while l < n:
            if (nums[l] & 1 == 1) or nums[l] > threshold:
                l += 1
                continue

            r = l + 1
            while r < n and nums[r] & 1 != nums[r - 1] & 1 and nums[r] <= threshold:
                r += 1

            max_len = max(max_len, r - l)
            l = r

        return max_len
