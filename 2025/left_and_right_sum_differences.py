"""
https://leetcode.com/problems/left-and-right-sum-differences/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def left_right_difference(self, nums: list[int]) -> list[int]:
        """
        left right difference
        """
        prefix_sums = list(accumulate(nums, initial=0))
        t = prefix_sums[0] + prefix_sums[-1]
        return [
            abs(prefix_sums[i] + prefix_sums[i - 1] - t)
            for i in range(1, len(nums) + 1)
        ]


print(Solution().left_right_difference([10, 4, 8, 3]))
