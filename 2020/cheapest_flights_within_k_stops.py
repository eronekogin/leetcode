"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""


from typing import List


from collections import deque


class Solution:
    def findCheapestPrice(
            self, n: int,
            flights: List[List[int]], src: int, dst: int, K: int) -> int:
        stops = [[] for _ in range(n)]
        for s, d, p in flights:  # Generate stops.
            stops[s].append((d, p))

        minPrice = float('inf')
        queue = deque([(src, 0, 0)])
        while queue:
            currStop, stopCnt, currSumPrice = queue.popleft()
            if currStop == dst:
                minPrice = min(minPrice, currSumPrice)
            elif stopCnt <= K and currSumPrice <= minPrice:
                for d, p in stops[currStop]:
                    queue.append((d, stopCnt + 1, currSumPrice + p))

        if minPrice == float('inf'):  # Not found.
            return -1

        return minPrice
