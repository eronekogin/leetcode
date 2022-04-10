"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
"""


from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Increasing 1 to all the n - 1 numbers = Decreasing 1 to the nth number.
        There is no point to decrease one to the current mininum number in nums
        and in the end all the numbers will be the same as the current mininum
        numbers after the decreasing steps.
        """
        return sum(nums) - len(nums) * min(nums)
