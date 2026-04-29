"""
https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/description/
"""


class Solution:
    """
    Solution
    """

    def max_oerations(self, nums: list[int]) -> int:
        """
        max operations
        """
        prev = nums[0] + nums[1]
        cnt = 1

        for i in range(2, len(nums), 2):
            if i + 1 >= len(nums) or nums[i] + nums[i + 1] != prev:
                break

            cnt += 1

        return cnt
