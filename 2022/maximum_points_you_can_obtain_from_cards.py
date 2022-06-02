"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        """
        The problem equals to find the minimum sum of subarray with length
        len(cardPoints) - k, so that the sum of remaining k cards in the
        list will be maximum when the total sum of the list is fixed.
        """
        maxLen = len(cardPoints) - k
        minSum = float('inf')
        start = currSum = 0
        for end, p in enumerate(cardPoints):
            currSum += p

            if end - start + 1 > maxLen:
                currSum -= cardPoints[start]
                start += 1

            if end - start + 1 == maxLen:
                minSum = min(minSum, currSum)

        return sum(cardPoints) - minSum
