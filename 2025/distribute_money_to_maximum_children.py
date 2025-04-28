"""
https://leetcode.com/problems/distribute-money-to-maximum-children/description/
"""


class Solution:
    """
    Solution
    """

    def dist_money(self, money: int, children: int) -> int:
        """
        dist money
        """
        if money < children:
            return -1

        q, r = divmod(money - children, 7)

        if q > children:
            return children - 1

        if q == children:
            return children - (r > 0)

        if q == children - 1 and r == 3:
            return q - 1

        return q
