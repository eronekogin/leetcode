"""
https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def find_prefix_score(self, nums: list[int]) -> list[int]:
        """
        find prefix score
        """
        curr_max = 0
        curr_sum = 0
        rslt: list[int] = []
        for x in nums:
            curr_max = max(curr_max, x)
            curr_sum += x + curr_max
            rslt.append(curr_sum)

        return rslt
