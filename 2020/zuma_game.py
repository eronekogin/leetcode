"""
https://leetcode.com/problems/zuma-game/
"""


from collections import Counter


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        maxBalls = len(hand) + 1
        remainBallsCounter = Counter(hand)

        def remove_single_group(currBoard: str) -> int:
            if not currBoard:  # Empty board.
                return 0

            totalUsedBalls = maxBalls
            start, end, maxLen = 0, 0, len(currBoard)
            while end < maxLen:
                currColor = currBoard[start]
                while end < maxLen and currBoard[end] == currColor:
                    end += 1

                # For consecutive balls on the board:
                # 1. If just 1 ball, need to use two balls with same color.
                # 2. If 2 balls, need to use 1 ball with same color.
                # 3. if 3 or more balls, no need to use any additional ball.
                currUsedBalls = 3 - min(3, end - start)
                if remainBallsCounter[currColor] >= currUsedBalls:
                    remainBallsCounter[currColor] -= currUsedBalls

                    # Just remove 1 sub group at a time in case the remaing
                    # sub groups could be combined together with the same
                    # color of balls.
                    totalUsedBalls = min(
                        totalUsedBalls, currUsedBalls + remove_single_group(
                            currBoard[:start] + currBoard[end:]))

                    remainBallsCounter[currColor] += currUsedBalls

                start = end
                end += 1

            return totalUsedBalls

        rslt = remove_single_group(board)

        # Cannot remove all the balls on the board after using all the balls
        # in hand.
        if rslt == maxBalls:
            return -1

        return rslt
