"""
https://leetcode.com/problems/shopping-offers/
"""


from typing import List, Tuple


class Solution:
    def shoppingOffers(
            self,
            price: List[int],
            special: List[List[int]],
            needs: List[int]) -> int:
        def get_lowest_cost(currNeeds: Tuple[int]) -> int:
            if currNeeds not in memo:
                n = len(currNeeds)

                # Calculate the cost without taking any offer.
                cost = sum(price[i] * currNeeds[i] for i in range(n))

                # Try to take any possible offer and get the lowest cost.
                for offer in special:
                    if all(currNeeds[i] >= offer[i] for i in range(n)):
                        remainNeeds = tuple(
                            currNeeds[i] - offer[i] for i in range(n))
                        cost = min(
                            cost, offer[-1] + get_lowest_cost(remainNeeds))

                memo[currNeeds] = cost

            return memo[currNeeds]

        memo = {}
        return get_lowest_cost(tuple(needs))


print(Solution().shoppingOffers(
    [2, 5],
    [[3, 0, 5], [1, 2, 10]],
    [3, 2]))
