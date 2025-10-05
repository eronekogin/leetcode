"""
https://leetcode.com/problems/account-balance-after-rounded-purchase/description/
"""


class Solution:
    """
    Solution
    """

    def account_balance_after_purchase(self, purchase_amount: int) -> int:
        """
        account balance after purchase
        """
        is_up_round = int((purchase_amount % 10) >= 5)

        return 100 - (purchase_amount // 10 + is_up_round) * 10
