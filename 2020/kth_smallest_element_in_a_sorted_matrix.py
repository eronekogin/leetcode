"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""


from typing import List
from heapq import heappush, heappop
from bisect import bisect_right


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Presumption: k is always valid.
        Use heap solution.
        """
        if not matrix or not matrix[0]:
            return None

        R, C = len(matrix), len(matrix[0])
        heap = []

        def push_item(r: int, c: int) -> None:
            if -1 < r < R and -1 < c < C:
                heappush(heap, (matrix[r][c], r, c))

        push_item(0, 0)
        cnt = 0
        while heap and cnt < k:
            rslt, r, c = heappop(heap)
            cnt += 1
            push_item(r, c + 1)
            if not c:
                push_item(r + 1, c)

        return rslt

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        """
        Use binary search solution.
        """
        if not matrix or not matrix[0]:
            return None

        start, end = matrix[0][0], matrix[-1][-1]
        while start < end:
            m = start + ((end - start) >> 1)
            total = 0
            for row in matrix:
                # bisect_right is to find how many numbers in the current
                # row that is <= m.
                total += bisect_right(row, m)

            if total < k:
                # This means m is too small and we need to find our
                # target value in [m + 1, end]
                start = m + 1
            else:
                # This means m is big enough for searching the target value.
                # In other words, the target value must exist in [start, m].
                # If total == k, we cannot say if m is our target value as
                # it could be possible that m does not exist in the matrix.
                # But again, our target value must exist in [start, m], so
                # we set end to m again to narrow the search in the next round.
                end = m

        # In the end start must be the same as the end, which means we have
        # found the target value.
        return start


matrix = [
    [1, 2],
    [3, 3]
]

print(Solution().kthSmallest2(matrix, 3))
