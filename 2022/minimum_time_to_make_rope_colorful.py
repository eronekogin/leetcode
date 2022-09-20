"""
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
"""


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        if len(colors) < 2:
            return 0

        prev = 0
        timeCost = 0
        for curr in range(1, len(colors)):
            if colors[curr] == colors[prev]:
                if neededTime[prev] > neededTime[curr]:
                    timeCost += neededTime[curr]
                else:
                    timeCost += neededTime[prev]
                    prev = curr
            else:
                prev = curr

        return timeCost


print(Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
