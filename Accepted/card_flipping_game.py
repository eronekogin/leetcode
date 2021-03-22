"""
https://leetcode.com/problems/card-flipping-game/
"""


class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        same = {x for x, y in zip(fronts, backs) if x == y}
        return min([i for i in fronts + backs if i not in same] or [0])
