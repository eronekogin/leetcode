"""
https://leetcode.com/problems/maximum-performance-of-a-team/
"""


from heapq import heappush, heappop


class Solution:
    def maxPerformance(
        self,
        n: int,
        speed: list[int],
        efficiency: list[int],
        k: int
    ) -> int:
        """
        1. Sort the efficiency from largest to smallest so that when we scan
            the list, at each loop we are getting the smallest efficiency
            in the current collected heap.
        2. Then in order to add the new member in, we simply pop out the 
            item with smallest speed, then calculate the performance at that
            time point.
        """
        heap = []
        maxPerformance = currSpeedSum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(heap, s)
            currSpeedSum += s
            if len(heap) > k:
                currSpeedSum -= heappop(heap)

            maxPerformance = max(maxPerformance, currSpeedSum * e)

        return maxPerformance % (10**9 + 7)


print(Solution().maxPerformance(6,
                                [2, 10, 3, 1, 5, 8],
                                [5, 4, 3, 9, 7, 2],
                                2))
