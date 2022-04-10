"""
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
"""


class Solution:
    def countOrders(self, n: int) -> int:
        """
        1. Number of ways to place pickups is N!
        2. Then valid number of ways to place deliver is
            1 * 3 * 5 * ... * (2N - 1)
        3. So the total number of ways is N! * (1 * 3 * ... * (2N - 1))
        """
        rslt = 1
        for i in range(1, n + 1):
            # Ways to arrange all pickups.
            rslt *= i

            # Ways to arrange all deliveries.
            rslt *= (i << 1) - 1

        return rslt % (10 ** 9 + 7)
