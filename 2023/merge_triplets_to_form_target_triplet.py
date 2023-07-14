"""
https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        a = b = c = 0
        x, y, z = target
        for a0, b0, c0 in triplets:
            if a0 <= x and b0 <= y and c0 <= z:
                a, b, c = max(a, a0), max(b, b0), max(c, c0)
        
        return [a, b, c] == target