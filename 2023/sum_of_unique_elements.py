"""
https://leetcode.com/problems/sum-of-unique-elements/
"""


from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        return sum([k for k, v in cnt.items() if v == 1] or [0])
