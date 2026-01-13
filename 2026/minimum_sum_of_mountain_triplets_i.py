"""
https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def minimum_sum(self, nums: list[int]) -> int:
        """
        Docstring for minimum_Sum

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :return: Description
        :rtype: int
        """
        n = len(nums)
        left_mins = [nums[0]] * n
        right_mins = [nums[-1]] * n

        for i in range(1, n):
            left_mins[i] = min(left_mins[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            right_mins[i] = min(right_mins[i + 1], nums[i])

        min_sum = 10 ** 5
        for i in range(1, n - 1):
            if nums[i] > left_mins[i] and nums[i] > right_mins[i]:
                min_sum = min(min_sum, nums[i] + left_mins[i] + right_mins[i])

        if min_sum == 10 ** 5:
            return -1

        return min_sum
