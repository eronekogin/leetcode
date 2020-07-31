"""
https://leetcode.com/problems/teemo-attacking/
"""


from typing import List


class Solution:
    def findPoisonedDuration(
            self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        totalPoisonTime = 0
        for i in range(len(timeSeries) - 1):
            totalPoisonTime += min(timeSeries[i + 1] - timeSeries[i], duration)

        return totalPoisonTime + duration


print(Solution().findPoisonedDuration([1, 4], 2))
