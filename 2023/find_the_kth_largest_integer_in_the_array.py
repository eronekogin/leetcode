"""
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
"""


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        return sorted(nums, key=lambda x: (len(x), x))[-k]