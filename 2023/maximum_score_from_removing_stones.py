"""
https://leetcode.com/problems/maximum-score-from-removing-stones/
"""


from heapq import heappush, heappop, heapify


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapify(heap)
        score = 0
        while len(heap) > 1:
            score += 1
            n1 = -heappop(heap)
            n2 = -heappop(heap)
            if n1 > 1:
                heappush(heap, -(n1 - 1))

            if n2 > 1:
                heappush(heap, -(n2 - 1))

        return score
