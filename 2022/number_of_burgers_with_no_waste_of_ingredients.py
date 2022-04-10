"""
https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
"""


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        """
        4a + 2b = tomatoSlcies
        a + b = cheeseSlices
        where a >= 0 and b >= 0, calculate the value of a and b.
        """
        a = tomatoSlices - (cheeseSlices << 1)
        if a < 0 or a & 1:
            return []

        a >>= 1
        if cheeseSlices < a:
            return []

        b = cheeseSlices - a
        return [a, b]
