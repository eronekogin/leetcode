"""
https://leetcode.com/problems/k-th-nearest-obstacle-queries/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """
    def results_array(self, queries: list[list[int]], k: int) -> list[int]:
        """
        results array
        """
        heap: list[int] = []
        rslt: list[int] = []

        for x, y in queries:
            if len(heap) < k:
                heappush(heap, -(abs(x) + abs(y)))
            elif abs(x) + abs(y) < -heap[0]:
                heappop(heap)
                heappush(heap, -(abs(x) + abs(y)))

            rslt.append(-1 if len(heap) < k else -heap[0])

        return rslt
