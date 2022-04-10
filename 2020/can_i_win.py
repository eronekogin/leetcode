"""
https://leetcode.com/problems/can-i-win/
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal < 2:  # First winner is guranteed to win.
            return True

        maxTotal = ((1 + maxChoosableInteger) * maxChoosableInteger) >> 1
        # The total sum of numbers are less than desiredTotal.
        if maxTotal < desiredTotal:
            return False

        # The total sum of numbers are equal to the desiredTotal, if the total
        # number is odd, the first player is guaranteed to win.
        if maxTotal == desiredTotal:
            return maxChoosableInteger & 1 == 1

        memo = {}  # state: bool to indicate win or not.

        def check(currTotal: int, state: int) -> bool:
            if state in memo:  # Already processed.
                return memo[state]

            for i in range(maxChoosableInteger):
                if not state & (1 << i):  # If the current number is not used.
                    # If no more number to pick for the next player or
                    # the next state leads to a lose for the next player, then
                    # the current player is guranteed to win with the current
                    # state.
                    if currTotal <= i + 1 or not check(
                            currTotal - i - 1, state | (1 << i)):
                        memo[state] = 1
                        return True

            # When reaching here, the current player cannot win in
            # any possible path.
            memo[state] = 0
            return False

        return check(desiredTotal, 0)


print(Solution().canIWin(4, 6))
