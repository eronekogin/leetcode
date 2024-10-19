"""
https://leetcode.com/problems/minimum-money-required-before-transactions/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_money(self, transactions: list[list[int]]) -> int:
        """
        minimum money
        """
        lost_money = sum(
            max(0, cost - profit)
            for cost, profit in transactions
        )

        # The worst case is we do all the transactions that will lose money, then
        # do all the transacitons that will gain money. For the first case, we
        # need to add the max profit because we need it to start this transaction;
        # For the second case, we just need the maximum cost to start the transaction.
        need_money = max(map(min, transactions))

        return lost_money + need_money


print(Solution().minimum_money([[2, 1], [5, 0], [4, 2]]))
