"""
https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/
"""


class Solution:
    def minOperationsMaxProfit(
        self,
        customers: list[int],
        boardingCost: int,
        runningCost: int
    ) -> int:
        if boardingCost * 4 <= runningCost:  # No positive profit.
            return -1

        i, n = 0, len(customers)
        rounds = maxRounds = profit = maxProfit = 0

        while i < n:
            waiting = minWaiting = 0

            # Check if there are enough customers.
            while i < n and waiting >= minWaiting:
                waiting += customers[i]
                minWaiting += 4
                i += 1

            # Calculate required rounds and profit.
            requiredRounds, waiting = divmod(waiting, 4)
            rounds += requiredRounds
            profit += requiredRounds * (4 * boardingCost - runningCost)

            if profit > maxProfit:
                maxProfit = profit
                maxRounds = rounds

            # If still having waiting customers.
            if waiting > 0 or requiredRounds == 0:
                rounds += 1
                profit += waiting * boardingCost - runningCost
                if profit > maxProfit:
                    maxProfit = profit
                    maxRounds = rounds

        if maxRounds > 0:
            return maxRounds

        return -1  # No positive profit.
