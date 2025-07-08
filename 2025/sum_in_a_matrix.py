"""
https://leetcode.com/problems/sum-in-a-matrix/description/
"""


class Solution:
    """
    Solution
    """

    def matrix_sum(self, nums: list[list[int]]) -> int:
        """
        matrix sum
        """
        for row in nums:
            row.sort()

        score = 0
        for c in range(len(nums[0])):
            score += max(nums[r][c] for r in range(len(nums)))

        return score
