"""
https://leetcode.com/problems/shuffle-the-array/
"""


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        rslt: list[int] = []
        N = len(nums) >> 1
        for i in range(N):
            rslt.extend([nums[i], nums[i + N]])

        return rslt
