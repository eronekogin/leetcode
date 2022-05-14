"""
https://leetcode.com/problems/reducing-dishes/
"""


class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        """
        1. We should cook the dishes that are most satisfied.
        2. We should put those most satisfied dishes to the end of the list
            so that the benifit from those dishes are maximized.
        """
        maxCoefficient = currCoefficient = 0
        sortedSatisfaction = sorted(satisfaction)
        while (
            sortedSatisfaction and
            sortedSatisfaction[-1] + currCoefficient > 0
        ):
            currCoefficient += sortedSatisfaction.pop()
            maxCoefficient += currCoefficient

        return maxCoefficient


print(Solution().maxSatisfaction([-1, -8, 0, 5, -9]))
