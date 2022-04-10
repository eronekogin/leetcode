"""
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
"""

from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(
            self, quality: list[int], wage: list[int], K: int) -> float:
        """
        1. Sort the ratio from w / q based on the quality and wage.
        2. For the same ratio, we could only afford lower quality people.
        3. Then maintain the K people with lower quality that we have seen so
            far, and get the minimum wage among them.
        """
        workers = sorted((w / q, q, w) for q, w in zip(quality, wage))
        rslt = float('inf')
        heap = []
        sumq = 0
        for ratio, q, w in workers:
            heappush(heap, -q)
            sumq += q
            if len(heap) > K:
                sumq += heappop(heap)

            if len(heap) == K:
                rslt = min(rslt, ratio * sumq)

        return rslt
