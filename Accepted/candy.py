"""
https://leetcode.com/problems/candy/
"""


from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n < 2:  # No kid or just 1 kid.
            return n

        rslt = [1] * n
        for i in range(1, n):  # Handle left neighbor for each kid.
            if ratings[i] > ratings[i - 1]:
                rslt[i] = rslt[i - 1] + 1

        candies = rslt[-1]
        for i in range(n - 2, -1, -1):  # Handle right neighbor for each kid.
            if ratings[i] > ratings[i + 1]:
                rslt[i] = max(rslt[i], rslt[i + 1] + 1)

            candies += rslt[i]

        return candies

    def count(self, n: int) -> int:
        return n * (n + 1) // 2

    def candy2(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n < 2:
            return n

        candies = up = down = oldSlope = 0
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                newSlope = 1  # Up
            elif ratings[i] < ratings[i - 1]:
                newSlope = -1  # Down
            else:
                newSlope = 0

            if (oldSlope > 0 and newSlope == 0) or \
                    (oldSlope < 0 and newSlope >= 0):
                candies += self.count(up) + self.count(down) + max(up, down)
                up = down = 0

            if newSlope > 0:
                up += 1
            elif newSlope < 0:
                down += 1
            else:
                candies += 1

            oldSlope = newSlope

        return candies + self.count(up) + self.count(down) + max(up, down) + 1
