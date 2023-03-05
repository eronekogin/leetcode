"""
https://leetcode.com/problems/car-fleet-ii/
"""


class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:
        """
        The question mentioned that each cars initial position is in
        ascending order, so suppose a, b, c cars are on the road, if a catches
        b, and b catches c, then a catches b + c. So we can scan from the end
        to the start of the cars and maitain a stack of index of cars, while
        their collision time are strictly in decreasing order.
        """
        stack: list[int] = []
        n = len(cars)
        rslt = [-1.0] * n

        for i in range(n - 1, -1, -1):
            position, speed = cars[i]
            while (
                stack and
                (
                    speed <= cars[stack[-1]][1] or (
                        (cars[stack[-1]][0] - position) /
                        (speed - cars[stack[-1]][1]) >= rslt[stack[-1]] > 0
                    )
                )
            ):
                stack.pop()

            if stack:
                rslt[i] = (
                    (cars[stack[-1]][0] - position) /
                    (speed - cars[stack[-1]][1])
                )

            stack.append(i)

        return rslt


print(Solution().getCollisionTimes([[1, 2], [2, 1], [4, 3], [7, 2]]))
