"""
https://leetcode.com/problems/random-pick-with-weight/
"""


from random import random
from bisect import bisect_left
from itertools import accumulate


class Solution:

    def __init__(self, w: List[int]):
        self.nums = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.nums, self.nums[-1] * random())
