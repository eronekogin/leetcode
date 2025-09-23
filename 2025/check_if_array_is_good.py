"""
https://leetcode.com/problems/check-if-array-is-good/description/
"""


class Solution:
    """
    Solution
    """

    def is_good(self, nums: list[int]) -> bool:
        """
        is good
        """
        nums.sort()
        n = nums[-1]

        return nums[:-1] == list(range(1, n + 1))
