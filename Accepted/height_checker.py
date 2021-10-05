"""
https://leetcode.com/problems/height-checker/
"""


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
