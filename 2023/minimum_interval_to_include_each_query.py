"""
https://leetcode.com/problems/minimum-interval-to-include-each-query/
"""


from heapq import heappush, heappop


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        sortedIntervals = sorted(intervals, reverse=True)
        heap = []
        memo = {}

        for q in sorted(queries):
            # collect candidate intervals having start <= q.
            while sortedIntervals and sortedIntervals[-1][0] <= q:
                start, end = sortedIntervals.pop()
                # Only add intervals having end >= q to the heap.
                if end >= q:
                    heappush(heap, (end - start + 1, end))

            # Clean up any interval from the heap that does not match the
            # current query.
            while heap and heap[0][1] < q:
                heappop(heap)

            if not heap:
                memo[q] = -1
            else:
                memo[q] = heap[0][0]

        return [memo[q] for q in queries]


print(Solution().minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))
