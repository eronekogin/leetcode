"""
https://leetcode.com/problems/furthest-building-you-can-reach/
"""


from heapq import heappush, heappop


class Solution:
    def furthestBuilding(
        self,
        heights: list[int],
        bricks: int,
        ladders: int
    ) -> int:
        """
        Use ladders to climb first and if not enough ladders at index i, we use
        bricks to fill the smallest gap from previous ladder filled gaps, so
        that we can have an extra ladder at index i to climb. If not enough
        bricks either, we return the current index.
        """
        heap = []
        for i in range(len(heights) - 1):
            delta = heights[i + 1] - heights[i]
            if delta > 0:
                heappush(heap, delta)

            if len(heap) > ladders:
                bricks -= heappop(heap)

            if bricks < 0:
                return i

        return len(heights) - 1


print(Solution().furthestBuilding(
    heights=[1, 5, 1, 2, 3, 4, 10000], bricks=4, ladders=1))
