"""
https://leetcode.com/problems/create-target-array-in-the-given-order/
"""


class Solution:
    def createTargetArray(
        self,
        nums: list[int],
        index: list[int]
    ) -> list[int]:
        rslt = []
        for x, i in zip(nums, index):
            rslt.insert(i, x)

        return rslt
