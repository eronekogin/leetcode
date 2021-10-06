"""
https://leetcode.com/problems/grumpy-bookstore-owner/
"""


class Solution:
    def maxSatisfied(
        self,
        customers: list[int],
        grumpy: list[int],
        minutes: int
    ) -> int:
        """
        Simply sliding window.
        """
        sumWithGrumpy = maxExtraCustomers = currExtraCustomers = 0
        for i, [customer, isGrumpy] in enumerate(zip(customers, grumpy)):
            sumWithGrumpy += customer * (1 - isGrumpy)
            currExtraCustomers += customer * isGrumpy

            if i >= minutes:  # Exceed the maximum window length.
                currExtraCustomers -= (
                    customers[i - minutes] * grumpy[i - minutes]
                )

            maxExtraCustomers = max(maxExtraCustomers, currExtraCustomers)

        return sumWithGrumpy + maxExtraCustomers


print(Solution().maxSatisfied(
    [1, 0, 1, 2, 1, 1, 7, 5],
    [0, 1, 0, 1, 0, 1, 0, 1],
    3
))
