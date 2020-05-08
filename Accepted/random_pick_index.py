"""
https://leetcode.com/problems/random-pick-index/
"""


from typing import List
from random import choice


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        return choice([i for i, n in enumerate(self.nums) if n == target])
