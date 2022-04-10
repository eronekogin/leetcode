"""
https://leetcode.com/problems/decompress-run-length-encoded-list/
"""


class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        rslt: list[int] = []
        for i in range(0, len(nums), 2):
            rslt.extend([nums[i + 1]] * nums[i])

        return rslt
