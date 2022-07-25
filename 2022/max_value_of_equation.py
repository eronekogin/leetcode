"""
https://leetcode.com/problems/max-value-of-equation/
"""


from heapq import heappush, heappop


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        """
        Since for all i < j, xi < xj, so equation yi + yj + |xi - xj| =
        yi + yj + xj - xi = (yi - xi) + (yj + xj)

        So in order to find the maximum value, we only need to find the
        maximum (yi - xi) while xj - xi <= k, so we could use a heap
        to do that.
        """
        heap = []
        rslt = float('-inf')
        for x, y in points:
            while heap and heap[0][1] < x - k:
                heappop(heap)

            if heap:
                rslt = max(
                    rslt,
                    x + y - heap[0][0]
                )

            heappush(heap, (x - y, x))

        return rslt
