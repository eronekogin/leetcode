"""
https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
"""


from heapq import heappush, heappop
from itertools import chain
from functools import cache


class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        def update(heap, num):
            if num not in heap:
                heappush(heap, num)
                if len(heap) > 3: heappop(heap)
        
        @cache
        def dp(i, j, dr):
            if not 0 <= i < n or not 0 <= j < m: return 0
            return dp(i-1, j+dr, dr) + grid[j][i]

        m, n, heap = len(grid), len(grid[0]), []
        
        # Check each single cell rhombus.
        for num in chain(*grid): update(heap, num)
        
        # Check larger rhombuses. q is the radius of the rhombus.
        for q in range(1, (1 + min(m, n))//2):
            for i in range(q, n - q):
                for j in range(q, m - q):
                    # upper right edge
                    p1 = dp(i + q, j, -1) - dp(i, j - q, -1)

                    # lower left edge
                    p2 = dp(i - 1, j + q - 1, -1) - dp(i - q - 1, j - 1, -1)

                    # upper left edge
                    p3 = dp(i, j - q, 1) - dp(i - q, j, 1)

                    # lower right edge
                    p4 = dp(i + q - 1, j + 1, 1) - dp(i - 1, j + q + 1, 1)

                    update(heap, p1 + p2 + p3 + p4)

        return sorted(heap)[::-1]