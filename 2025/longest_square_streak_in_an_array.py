"""
https://leetcode.com/problems/longest-square-streak-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def longest_square_streak(self, nums: list[int]) -> int:
        """
        longest square streak
        """
        candidates = set(nums)
        max_num = max(candidates)
        max_len = -1

        for x in sorted(candidates):
            curr_len = 0
            next_num = x * x
            while next_num <= max_num and next_num in candidates:
                next_num *= next_num
                curr_len += 1

            if curr_len > 0:
                max_len = max(max_len, curr_len + 1)

        return max_len
