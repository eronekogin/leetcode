"""
https://leetcode.com/problems/add-minimum-number-of-rungs/
"""

class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        total = [0] + rungs
        return sum((b - 1 - a) // dist for a, b in zip(total, total[1:]) if b - a > dist)