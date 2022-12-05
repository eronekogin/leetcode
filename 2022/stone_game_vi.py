"""
https://leetcode.com/problems/stone-game-vi/
"""


class Solution:
    def stoneGameVI(
        self,
        aliceValues: list[int],
        bobValues: list[int]
    ) -> int:
        """
        Assume bob takes all the stones at first, the total difference is
        sum(bobValues) now. Then for each stone Alice is picking:
            newDifference = difference + aliceValues[i] + bobValues[i]

        So in order to play optimally, alice and bob will pick the stone
        having the current maximum aliceValues[i] + bobValues[i].
        """
        rslt = (
            sum(sorted(a + b for a, b in zip(aliceValues, bobValues))[::-2]) -
            sum(bobValues)
        )
        if rslt > 0:
            return 1

        if rslt < 0:
            return -1

        return 0
