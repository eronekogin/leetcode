"""
https://leetcode.com/problems/moving-stones-until-consecutive/
"""


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        sa, sb, sc = sorted([a, b, c])
        # Maximum of moves come from the number of empty positions between the
        # max and the min value among a, b and c.
        maxMoves = sc - sa - 1 - 1

        # Calculate minimum moves.
        if sb - sa == sc - sb == 1:
            # When originally a, b, c is consecutive, the minimum move is zero.
            minMoves = 0
        elif sb - sa == 1 or sc - sb == 1:
            # When originally a, b or b, c is consecutive, the minimum move is
            # one.
            minMoves = 1
        elif sb - sa == 2 or sc - sb == 2:
            # When originally between a, b or b, c there is only 1 empty slot.
            minMoves = 1
        else:
            # We could always move sc to the right position of sb, then
            # move sa to the left position of sb.
            minMoves = 2

        return [minMoves, maxMoves]
