"""
https://leetcode.com/problems/minimum-absolute-difference/
"""


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        sortedArr = sorted(arr)
        minDiff = sortedArr[1] - sortedArr[0]
        pairs = [sortedArr[:2]]
        for i in range(2, len(sortedArr)):
            if sortedArr[i] - sortedArr[i - 1] < minDiff:
                minDiff = sortedArr[i] - sortedArr[i - 1]
                pairs = [[sortedArr[i - 1], sortedArr[i]]]
            elif sortedArr[i] - sortedArr[i - 1] == minDiff:
                pairs.append([sortedArr[i - 1], sortedArr[i]])

        return pairs
