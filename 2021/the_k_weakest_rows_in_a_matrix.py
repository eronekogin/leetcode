"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        return [
            i
            for _, i in sorted((sum(row), i) for i, row in enumerate(mat))[:k]]
