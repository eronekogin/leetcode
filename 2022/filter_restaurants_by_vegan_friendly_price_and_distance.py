"""
https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
"""


class Solution:
    def filterRestaurants(
        self,
        restaurants: list[list[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int
    ) -> list[int]:
        candidates = [
            x
            for x in restaurants
            if x[3] <= maxPrice and x[4] <= maxDistance
        ]

        if veganFriendly:
            candidates = [
                x
                for x in candidates
                if x[2]
            ]

        return [
            x[0]
            for x in sorted(candidates, key=lambda x: (-x[1], -x[0]))
        ]
