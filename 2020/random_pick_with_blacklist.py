"""
https://leetcode.com/problems/random-pick-with-blacklist/
"""


from typing import List


from random import random


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        excludes = {num: num for num in blacklist}
        maxPick, swapNum = N - len(blacklist), N - 1
        for num in blacklist:
            if num < maxPick:
                # The excluded number is inside the picking range, swap it
                # with the first not excluded number starting from the
                # tail of the non-picking range.
                while swapNum in excludes:
                    swapNum -= 1

                excludes[num] = swapNum
                swapNum -= 1

        self._excludes = excludes
        self._maxPick = maxPick

    def pick(self) -> int:
        # Simply pick a number randomly from the non-blocking range.
        x = int(random() * self._maxPick)
        if x in self._excludes:
            return self._excludes[x]

        return x
