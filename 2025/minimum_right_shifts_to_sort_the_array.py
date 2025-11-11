"""
https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_right_shifts(self, nums: list[int]) -> int:
        """
        minimum right shifts
        """
        n = len(nums)
        sorted_nums = sorted(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if nums[i:] + nums[:i] == sorted_nums:
                    return n - i

                return -1

        return 0  # Already sorted


print(Solution().minimum_right_shifts([2, 1, 4]))
