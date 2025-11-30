"""
https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def max_subarrays(self, nums: list[int]) -> int:
        """
        max subarrays
        """
        curr_score = -1  # all digits are 1
        rslt = 0

        for x in nums:
            curr_score &= x
            if curr_score == 0:
                curr_score = -1
                rslt += 1  # make a new split

        # In case no split, which means the score of
        # all numbers in nums is positive, we don't
        # need to split array at all since the score
        # of any subarrary of nums will be greater than
        # the score of nums
        return max(1, rslt)
