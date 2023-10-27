"""
https://leetcode.com/problems/maximum-difference-between-increasing-elements/
"""


class Solution:
    """
    Solution
    """

    def maximum_difference(self, nums: list[int]) -> int:
        """
        maximum_difference
        """
        max_diff = -1
        min_num = nums[0]
        for num in nums:
            max_diff = max(max_diff, num - min_num)
            min_num = min(min_num, num)

        if max_diff == 0:
            return -1

        return max_diff


print(Solution().maximum_difference([9, 4, 3, 2]))
