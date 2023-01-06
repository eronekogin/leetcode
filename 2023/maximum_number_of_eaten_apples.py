"""
https://leetcode.com/problems/maximum-number-of-eaten-apples/
"""

from heapq import heappush, heappop


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        heap = []
        maxApples = 0
        i, N = 0, len(apples)
        while i < N or heap:
            if i < N and apples[i] > 0:
                heappush(heap, [i + days[i], apples[i]])

            while heap and (heap[0][0] <= i or heap[0][1] == 0):
                heappop(heap)

            if heap:
                heap[0][1] -= 1
                maxApples += 1

            i += 1

        return maxApples
