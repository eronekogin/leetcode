"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""


from typing import List
from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(
            self,
            nums1: List[int],
            nums2: List[int],
            k: int) -> List[List[int]]:
        """
            1 1 2  -- nums1
         1  2 2 3
         2  3 3 4
         3  4 4 5
         |
         nums2
        """
        sumHeap = []
        N1, N2 = len(nums1), len(nums2)

        def push(r: int, c: int) -> None:
            if r < N1 and c < N2:
                heappush(sumHeap, (nums1[r] + nums2[c], r, c))

        pairs = []
        push(0, 0)  # Move top-left element into the heap.
        while sumHeap and len(pairs) < k:
            _, r, c = heappop(sumHeap)
            pairs.append([nums1[r], nums2[c]])
            push(r, c + 1)  # Move its left element into the heap.
            if not c:
                # When the current element is the leftmost one in its row.
                push(r + 1, c)  # Move its down element into the heap.

        return pairs
