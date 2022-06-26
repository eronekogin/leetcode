"""
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
"""


from collections import Counter


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)
