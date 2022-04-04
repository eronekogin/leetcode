"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
"""

from heapq import heapify, heappop, heappush


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        """
        1. Genearal idea is from the target list, find the current maximum
            value, then subtract it from the sum of remaining numbers, which
            could give us the last number that were used in the last round.
            Then we recursively do this until we cannot.
        2. In case the current maximum number is too large comparing to the
            sum of other numbers, we could use the % to accelarate the process
            in one calculation so that the current maximum number will no
            longer be maximum.
        """
        total = sum(target)
        heap = [-num for num in target]
        heapify(heap)
        while True:
            currMax = -heappop(heap)  # Get current maximum number.
            total -= currMax  # Get the sum of remaining numbers.

            # Case 1: if the target list only contains 1.
            # Case 2: if the sum of remaining numbers is 1.
            if currMax == 1 or total == 1:
                return True

            # If remaining sum is not large enough.
            if currMax < total or total == 0 or currMax % total == 0:
                return False

            # Subract the current maximum number and push it back to heap.
            currMax %= total
            total += currMax
            heappush(heap, -currMax)
