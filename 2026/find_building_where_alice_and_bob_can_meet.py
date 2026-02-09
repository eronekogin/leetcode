"""
https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description/
"""


from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    """
    Docstring for Solution
    """

    def leftmost_building_queries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        """
        Docstring for leftmost_building_queries

        :param self: Description
        :param heights: Description
        :type heights: list[int]
        :param queries: Description
        :type queries: list[List[int]]
        :return: Description
        :rtype: list[int]
        """
        heap: list[tuple[int, int]] = []
        rslt = [-1] * len(queries)
        unhandled_queries: defaultdict[
            int,
            list[tuple[int, int]]
        ] = defaultdict(list)

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a

            if heights[b] > heights[a]:
                rslt[i] = b
            elif a == b:
                rslt[i] = a
            else:
                unhandled_queries[b].append((heights[a], i))

        for i, h in enumerate(heights):
            while heap and heap[0][0] < h:
                _, j = heappop(heap)
                rslt[j] = i

            for item in unhandled_queries[i]:
                heappush(heap, item)

        return rslt
