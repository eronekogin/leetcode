"""
https://leetcode.com/problems/semi-ordered-permutation/description/
"""


class Solution:
    """
    Solution
    """

    def semi_ordered_permutation(self, nums: list[int]) -> int:
        """
        semi ordered permutation
        """
        n = len(nums)
        first = nums.index(1)
        last = nums.index(n)
        return first + n - 1 - last - (first > last)
