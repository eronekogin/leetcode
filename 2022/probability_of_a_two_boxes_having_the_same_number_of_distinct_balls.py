"""
https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/
"""


from math import factorial


class Solution:
    def getProbability(self, balls: list[int]) -> float:
        def get_dinstinct_permutation(
            totalLen: int,
            dupList: list[int]
        ) -> int:
            p = 1
            for k in dupList:
                p *= factorial(k)

            return factorial(totalLen) // p

        def dfs(i: int, s1: int, s2: int, c1: int, c2: int) -> None:
            if abs(s1 - s2) > totalBalls - s1 - s2:
                # Not enough remaining balls to be divided.
                return

            if i == len(balls):  # Used all balls.
                if s1 != s2:  # Not equal balls in two boxes.
                    return

                p1 = get_dinstinct_permutation(s1, firstBox.values())
                p2 = get_dinstinct_permutation(s2, secondBox.values())
                total = p1 * p2
                self.all += total
                self.good += total * (c1 == c2)
            else:  # Divide the current color.
                for j in range(balls[i] + 1):
                    firstBox[i], secondBox[i] = j, balls[i] - j
                    dfs(
                        i + 1,
                        s1 + j,
                        s2 + balls[i] - j,
                        c1 + (j != 0),
                        c2 + (j != balls[i])
                    )

        firstBox = {}
        secondBox = {}
        totalBalls = sum(balls)
        self.good = 0
        self.all = 0
        dfs(0, 0, 0, 0, 0)
        return self.good / self.all
