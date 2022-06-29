"""
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""


class Solution:
    def maxArea(
        self,
        h: int,
        w: int,
        horizontalCuts: list[int],
        verticalCuts: list[int]
    ) -> int:
        sortedHCuts = sorted(horizontalCuts)
        sortedVCuts = sorted(verticalCuts)
        maxHInterval = max(
            [
                b - a
                for a, b in zip(sortedHCuts, sortedHCuts[1:])
            ] or [0]
        )
        maxHInterval = max(maxHInterval, sortedHCuts[0], h - sortedHCuts[-1])

        maxVInterval = max(
            [
                b - a
                for a, b in zip(sortedVCuts, sortedVCuts[1:])
            ] or [0]
        )
        maxVInterval = max(maxVInterval, sortedVCuts[0], w - sortedVCuts[-1])

        return (maxHInterval * maxVInterval) % (10 ** 9 + 7)
