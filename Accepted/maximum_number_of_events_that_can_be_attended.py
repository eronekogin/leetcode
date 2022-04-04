"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
"""


from heapq import heappush, heappop


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        sortedEvents = sorted(events, reverse=True)
        heap = []
        cnt = currDay = 0
        while sortedEvents or heap:
            if not heap:
                currDay = sortedEvents[-1][0]

            # Add all events' end day to heap for any
            # events' start day <= current day.
            while sortedEvents and sortedEvents[-1][0] <= currDay:
                heappush(heap, sortedEvents.pop()[1])

            # Attend the event that ends soonest for the current day.
            heappop(heap)
            cnt += 1

            # Go to the next day and remove all events that already ends
            # before the next day from the heap.
            currDay += 1
            while heap and heap[0] < currDay:
                heappop(heap)

        return cnt
