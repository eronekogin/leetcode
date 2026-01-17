"""
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def sum_counts(self, nums: list[int]) -> int:
        """
        Docstring for sum_counts

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :return: Description
        :rtype: int
        """
        square_sum = 0
        for i in range(len(nums)):
            distincts: set[int] = set()
            for j in range(i, len(nums)):
                distincts.add(nums[j])
                square_sum += len(distincts) * len(distincts)

        return square_sum


print(Solution().sum_counts([1, 2, 1]))
