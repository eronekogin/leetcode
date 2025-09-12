"""
https://leetcode.com/problems/longest-alternating-subarray/description/
"""


class Solution:
    """
    Solution
    """

    def alternating_subarray(self, nums: list[int]) -> int:
        """
        alternating subarray
        """
        max_len = 1
        n = len(nums)
        start = 0
        while start < n - 1:
            end = start + 1
            while end < n and nums[end] == nums[start] + ((end - start) & 1):
                end += 1

            max_len = max(max_len, end - start)
            start = max(start + 1, end - 1)

        if max_len == 1:
            return -1

        return max_len


print(Solution().alternating_subarray([2, 3, 4, 3, 4]))
