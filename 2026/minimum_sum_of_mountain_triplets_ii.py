"""
https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def minimum_sum(self, nums: list[int]) -> int:
        """
        Docstring for minimum_sum

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :return: Description
        :rtype: int
        """
        n = len(nums)
        lefts = [nums[0]] * n
        rights = [nums[-1]] * n

        for i in range(1, n):
            lefts[i] = min(nums[i], lefts[i - 1])

        for i in range(n - 2, -1, -1):
            rights[i] = min(nums[i], rights[i + 1])

        min_sum = 10 ** 10
        for i in range(1, n - 1):
            if nums[i] > lefts[i] and nums[i] > rights[i]:
                min_sum = min(min_sum, nums[i] + lefts[i] + rights[i])

        if min_sum == 10 ** 10:
            return -1

        return min_sum
