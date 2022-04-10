"""
https://leetcode.com/problems/trapping-rain-water-ii/
"""


from typing import List
from heapq import heappush, heappop


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        In trapping-rain-water-i we are dealing with a 1d array so
        our pointers just come from the left or right side. However in
        this question our candidate pointer comes from 4 directions so
        a heap is helpful to determine which direction has the lowest height.
        """
        if not heightMap or not heightMap[0]:
            return 0

        R, C = len(heightMap), len(heightMap[0])
        heap, visited = [], [[0] * C for _ in range(R)]

        # First add all the elements on the boarder to heap.
        for r in range(R):
            for c in range(C):
                if r in {0, R - 1} or c in {0, C - 1}:
                    heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = 1

        # Then try to determine the lowest pointer.
        water = 0
        while heap:
            h, r, c = heappop(heap)
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    nh = heightMap[nr][nc]
                    water += max(0, h - nh)
                    heappush(heap, (max(h, nh), nr, nc))
                    visited[nr][nc] = 1

        return water
