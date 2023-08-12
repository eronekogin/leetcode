"""
https://leetcode.com/problems/concatenation-of-array/
"""


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums[:]