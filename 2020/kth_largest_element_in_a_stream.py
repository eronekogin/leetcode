"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""


from typing import List


from heapq import heappush, heappop


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        h = []
        for num in nums:
            heappush(h, num)
            if len(h) > k:
                heappop(h)

        self._heap = h
        self._maxLen = k

    def add(self, val: int) -> int:
        h = self._heap
        heappush(h, val)
        if len(h) > self._maxLen:
            heappop(h)

        return h[0]


s = KthLargest(3, [4, 5, 8, 2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))
