"""
https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_time(self, s: str) -> int:
        """
        minimum time
        """
        min_left_cost = 0
        rslt = n = len(s)
        for i, c in enumerate(s):
            min_left_cost = min(
                min_left_cost + (c == '1') * 2,  # Remove ith car
                i + 1  # Remove all previous cars from 0 to i
            )

            # minimum cost is min_left + cost to remove all right cars, which is
            # n - 1 - i. Notice that if there is a less cost from right side,
            # it will still be covered by the calculation of min_left_cost.
            rslt = min(
                rslt,
                min_left_cost + n - 1 - i
            )

        return rslt
