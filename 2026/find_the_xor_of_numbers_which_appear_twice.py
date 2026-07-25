"""
https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/
"""


class Solution:
    """
    Solution
    """

    def duplicate_numbers_xor(self, nums: list[int]) -> int:
        """
        duplicate numbers xor
        """
        memo: set[int] = set()
        rslt = 0
        for x in nums:
            if x not in memo:
                memo.add(x)
            else:
                rslt ^= x

        return rslt
