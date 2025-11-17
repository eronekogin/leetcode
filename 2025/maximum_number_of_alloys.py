"""
https://leetcode.com/problems/maximum-number-of-alloys/description/
"""


from bisect import bisect_left


class Solution:
    """
    Solution
    """

    def max_number_of_alloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: list[list[int]],
        stock: list[int],
        cost: list[int]
    ) -> int:
        """
        max number of alloys
        """
        def check(x: int) -> bool:
            for comp in composition:
                extra_cost = sum(
                    max(0, amount * x - s) * c
                    for amount, s, c in zip(comp, stock, cost)
                )

                if extra_cost <= budget:
                    return False

            return True

        check_range = range(min(stock) + budget + 1)
        return bisect_left(check_range, True, key=check) - 1
