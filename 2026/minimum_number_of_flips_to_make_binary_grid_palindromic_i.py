"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/description/
"""


class Solution:
    """
    Solution
    """

    def min_flips(self, grid: list[list[int]]) -> int:
        """
        min flips
        """
        def count_flips(nums: list[int]) -> int:
            l, r = 0, len(nums) - 1
            flips = 0
            while l < r:
                flips += nums[l] != nums[r]
                l += 1
                r -= 1

            return flips

        row_flips = sum(count_flips(row) for row in grid)
        col_flips = sum(count_flips(list(col)) for col in zip(*grid))
        return min(row_flips, col_flips)
