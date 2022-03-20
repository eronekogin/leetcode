"""
https://leetcode.com/problems/rank-transform-of-an-array/
"""


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rankMap = {num: (i + 1) for i, num in enumerate(sorted(set(arr)))}
        return [rankMap[num] for num in arr]
