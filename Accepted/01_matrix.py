"""
https://leetcode.com/problems/01-matrix/
"""


from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Simple BFS starting from the list of all cells with zero values.
        """
        R, C = len(matrix), len(matrix[0])
        distances = [[None] * C for _ in range(R)]
        queue = deque()

        # Collect zero cells and set distances.
        for r in range(R):
            for c in range(C):
                if not matrix[r][c]:
                    distances[r][c] = 0
                    queue.append((r, c))

        # Scan the neighbours of each zero cell and set distances.
        while queue:
            r, c = queue.popleft()
            currDistance = distances[r][c]
            for ar, ac in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= ar < R and 0 <= ac < C and distances[ar][ac] is None:
                    distances[ar][ac] = 1 + currDistance
                    queue.append((ar, ac))

        return distances


print(Solution().updateMatrix(
    [
        [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
    ]))
