"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""


from typing import List


from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heappush(heap, (-(x * x + y * y), x, y))
            if len(heap) > K:
                heappop(heap)

        rslt = []
        while heap:
            rslt.append(heappop(heap)[1:])

        return rslt
