"""
https://leetcode.com/problems/sum-of-beauty-in-the-array/
"""


class Solution:
    """
    Solution
    """

    def sum_of_beauties(self, nums: list[int]) -> int:
        """
        sum_of_beauties
        """
        n = len(nums)
        left_max_nums: list[int] = [nums[0]] * n
        right_min_nums: list[int] = [nums[-1]] * n

        for i in range(1, n):
            left_max_nums[i] = max(left_max_nums[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            right_min_nums[i] = min(right_min_nums[i + 1], nums[i])

        rslt = 0
        for i in range(1, n - 1):
            if left_max_nums[i - 1] < nums[i] < right_min_nums[i + 1]:
                rslt += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                rslt += 1

        return rslt
