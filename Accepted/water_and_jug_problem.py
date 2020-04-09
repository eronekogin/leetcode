"""
https://leetcode.com/problems/water-and-jug-problem/
"""


from fractions import gcd


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        """
        The jug operations could only result in the following comnbinations,
        assume x < y:

        R1: y + x, y, y - x, y - 2x, ... , y % x
        R2: y + y % x, y + y % x - x, y + y % x - 2x, ..., 2y % x
        R3: y + 2y % x, ..., 3y % x
        ...
        RX: y + (x - 1)y % x, ..., xy % x

        Since xy % x = 0, now for the x + 1 round, we are back to the initial
        states where both jug x and jug y are empty. Then we start at R1 again.

        So basically z could only be a combination of ax + by, while a, b
        are integers. Then the restrictions will be:

        1. z should be divisible by the gcd(x, y).
        2. x + y must be greater or equal than z in order to hold all the z
            litres water at the end of the final operation.
        """
        return z == 0 or x + y >= z and z % gcd(x, y) == 0
