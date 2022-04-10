"""
https://leetcode.com/problems/last-stone-weight/
"""


from typing import List


from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-x for x in stones]
        heapify(stoneHeap)
        while len(stoneHeap) > 1:
            s1 = heappop(stoneHeap)
            s2 = heappop(stoneHeap)
            heappush(stoneHeap, s1 - s2)

        return -heappop(stoneHeap)
