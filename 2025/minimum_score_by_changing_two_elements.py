"""
https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/
"""


class Solution:
    """
    Solution
    """

    def minimize_sum(self, nums: list[int]) -> int:
        """
        After sorting, three cases could happen:
            * Change the leftmost two nums to be the same as the maximum number
            * Change the rightmost two nums to be the same as the minimum number
            * Change the leftmost to its right an the rigtmost to its left
        """
        nums.sort()

        return min(
            nums[-1] - nums[2],
            nums[-3] - nums[0],
            nums[-2] - nums[1]
        )
