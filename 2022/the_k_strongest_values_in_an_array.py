"""
https://leetcode.com/problems/the-k-strongest-values-in-an-array/
"""

from heapq import heappush, heappop


class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        # Get median.
        m = sorted(arr)[(len(arr) - 1) >> 1]

        heap: list[tuple[int]] = []

        for num in arr:
            heappush(heap, (abs(num - m), num))
            if len(heap) > k:
                heappop(heap)

        return [num for _, num in heap]
