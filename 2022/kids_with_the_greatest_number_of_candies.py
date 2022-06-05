"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""


class Solution:
    def kidsWithCandies(
        self,
        candies: list[int],
        extraCandies: int
    ) -> list[bool]:
        maxCandy = max(candies)
        return [x + extraCandies >= maxCandy for x in candies]
