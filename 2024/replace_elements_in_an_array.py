"""
https://leetcode.com/problems/replace-elements-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def array_change(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        """
        array change
        """
        memo = {x: i for i, x in enumerate(nums)}
        rslt = list(nums)

        for x, y in operations:
            i = memo[x]
            memo[y] = i
            rslt[i] = y

        return rslt
