"""
https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
"""


class Solution:
    def trimMean(self, arr: list[int]) -> float:
        sortedArr = sorted(arr)
        N = len(arr)
        removeLimit = N * 5 // 100
        remainingArr = sortedArr[removeLimit: N - removeLimit]
        return sum(remainingArr) / len(remainingArr)
