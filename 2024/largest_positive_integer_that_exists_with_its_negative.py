"""
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
"""


class Solution:
    """
    Solution
    """

    def find_max_k(self, nums: list[int]) -> int:
        """
        find max k
        """
        memo = set(nums)
        rslt = -1

        for x in memo:
            if x > 0 and -x in memo:
                rslt = max(rslt, x)

        return rslt
