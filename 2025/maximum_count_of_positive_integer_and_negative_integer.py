"""
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_count(self, nums: list[int]) -> int:
        """
        maximum count
        """
        negatives = zeros = 0
        for x in nums:
            if x < 0:
                negatives += 1
            elif x == 0:
                zeros += 1
            else:
                break

        return max(negatives, len(nums) - negatives - zeros)
