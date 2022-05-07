"""
https://leetcode.com/problems/find-lucky-integer-in-an-array/
"""


from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        cnt = Counter(arr)
        return max([x for x in cnt if x == cnt[x]] or [-1])
