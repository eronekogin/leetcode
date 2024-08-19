"""
https://leetcode.com/problems/design-a-food-rating-system/description/
"""


from collections import defaultdict
from heapq import heappop, heappush


class FoodRatings:
    """
    Food Ratings
    """

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisine_to_heap: defaultdict[
            str,
            list[tuple[int, str]]
        ] = defaultdict(list)
        self.food_to_cuisine: dict[str, str] = {}
        self.food_to_rating: dict[str, int] = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            heappush(self.cuisine_to_heap[c], (-r, f))
            self.food_to_rating[f] = -r

    def change_rating(self, food: str, new_rating: int) -> None:
        """
        change rating
        """
        c = self.food_to_cuisine[food]
        heappush(self.cuisine_to_heap[c], (-new_rating, food))
        self.food_to_rating[food] = -new_rating

    def highest_rated(self, cuisine: str) -> str:
        """
        highest rated
        """
        h = self.cuisine_to_heap[cuisine]
        while h[0][0] != self.food_to_rating[h[0][1]]:
            # lazy delete old data when actually queried.
            heappop(h)

        return h[0][1]
