"""
https://leetcode.com/problems/calculate-amount-paid-in-taxes/description/
"""


class Solution:
    """
    Solution
    """

    def calculate_tax(self, brackets: list[list[int]], income: int) -> float:
        """
        calculate tax
        """
        tax = 0
        prev = 0
        for bound, percent in brackets:
            tax += (min(bound, income) - prev) * percent / 100
            if bound > income:
                break

            prev = bound

        return tax
