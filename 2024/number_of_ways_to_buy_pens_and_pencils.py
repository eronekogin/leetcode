"""
https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/description/
"""


class Solution:
    """
    Solution
    """

    def ways_to_buy_pens_pencils(self, total: int, cost1: int, cost2: int) -> int:
        """
        ways to buy pens pencils
        """
        cnt = 0
        for a in range(total // cost1 + 1):
            cnt += (total - a * cost1) // cost2 + 1

        return cnt
