"""
https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def min_number_of_seconds(self, mountain_height: int, worker_times: list[int]) -> int:
        """
        min number of seconds
        """
        heap = [(t, t, 1) for t in worker_times]
        heapify(heap)

        for _ in range(mountain_height):
            next_cost, original_cost, picked_up = heappop(heap)

            picked_up += 1
            next_cost += original_cost * picked_up
            heappush(heap, (next_cost, original_cost, picked_up))

        rslt = 0
        while heap:
            next_cost, original_cost, picked_up = heappop(heap)
            rslt = max(rslt, next_cost - original_cost * picked_up)

        return rslt
