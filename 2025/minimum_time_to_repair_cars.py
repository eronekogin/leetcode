"""
https://leetcode.com/problems/minimum-time-to-repair-cars/description/
"""


from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def repair_cars(self, ranks: list[int], cars: int) -> int:
        """
        repair cars
        """
        heap = [
            (rank, rank, 1, workers)
            for rank, workers in Counter(ranks).items()
        ]

        heapify(heap)

        while cars > 0:
            t, r, n, workers = heappop(heap)

            cars -= workers
            n += 1
            heappush(heap, (r * n * n, r, n, workers))

        return t
