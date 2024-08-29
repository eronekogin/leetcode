"""
https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/
"""


from math import ceil


class Solution:
    """
    Solution
    """

    def minimum_replacement(self, nums: list[int]) -> int:
        """
        minimum replacement
        """
        ops = 0
        curr_max = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            x = nums[i]

            k = ceil(x / curr_max)
            ops += k - 1
            curr_max = x // k

        return ops


print(Solution().minimum_replacement([2, 10, 20, 19, 1]))
