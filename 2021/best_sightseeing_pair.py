"""
https://leetcode.com/problems/best-sightseeing-pair/
"""


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        1. The goal is to find the maximum distance calculated from
            values[i] + i + values[j] - j if i < j.
        2. So we should keep the previous best values[i] + i, and if we
            find the current j is better than i, we update i with j.
        """
        maxScore = values[0]
        prevBestIdx = 0
        prevBestSum = values[prevBestIdx] + prevBestIdx
        for j in range(1, len(values)):
            maxScore = max(
                maxScore, prevBestSum + values[j] - j)
            if values[j] + j > prevBestSum:
                prevBestIdx = j
                prevBestSum = values[j] + j

        return maxScore
