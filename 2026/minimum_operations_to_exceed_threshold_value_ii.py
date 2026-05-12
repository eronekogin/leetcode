"""
https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int], k: int) -> int:
        """
        min operations
        """
        heap: list[int] = list(nums)
        heapify(heap)
        ops = 0

        while len(heap) >= 2 and heap[0] < k:
            x = heappop(heap)
            y = heappop(heap)
            heappush(heap, (x << 1) + y)
            ops += 1

        return ops
