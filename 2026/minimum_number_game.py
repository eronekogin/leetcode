"""
https://leetcode.com/problems/minimum-number-game/description/
"""


class Solution:
    """
    Solution
    """

    def number_game(self, nums: list[int]) -> list[int]:
        """
        number game
        """
        rslt: list[int] = []
        sorted_nums = sorted(nums)
        for i in range(0, len(nums) - 1, 2):
            rslt.append(sorted_nums[i + 1])
            rslt.append(sorted_nums[i])

        return rslt
