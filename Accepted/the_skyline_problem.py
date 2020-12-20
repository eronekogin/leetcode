"""
https://leetcode.com/problems/the-skyline-problem/


https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms

Since python's heap's top always return the smallest item in the heap,
so we have to store the negative height in order to get back the current
maximum height in the heap.
"""


from typing import List
from heapq import heappush, heappop


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        There are two kind of events:
        1. Buiding start: (startPos, height, endPos)
        2. Buiding end: (startPos, 0, 0)

        Scanning the building list and create the events list, then
        sort them from left to right.
        """
        events = [(l, -h, r) for l, r, h in buildings]  # Building start.
        events += list({(r, 0, 0) for _, r, _ in buildings})  # Building end.
        events.sort()

        rslt = [[0, 0]]  # [startPos, height]
        heap = [(0, float('inf'))]  # [height, endPos]
        for l, negH, r in events:
            # Keep popping the max height items from the heap
            # when the item's end position is <= the current position.
            while l >= heap[0][1]:
                heappop(heap)

            # If the current event is a building start event,
            # push the item to the heap.
            if negH:
                heappush(heap, (negH, r))

            # If the previous key point's height is different than
            # the current smallest heap in the heap, add a new
            # key point to the result list.
            h = heap[0][0]
            if rslt[-1][1] + h:  # rslt[-1][1] == -h.
                rslt.append((l, -h))

        return rslt[1:]
