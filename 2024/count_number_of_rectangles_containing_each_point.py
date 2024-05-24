"""
https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/description/
"""


from bisect import bisect_left
from collections import defaultdict


class Solution:
    """
    Solution
    """

    def count_rectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
        """
        count rectangles
        """
        heights: defaultdict[int, list[int]] = defaultdict(list)
        for l, h in rectangles:
            heights[h].append(l)

        for v in heights.values():
            v.sort()

        return [
            sum(
                len(heights[y]) - bisect_left(heights[y], x)
                for y in range(y, 101)
                if y in heights
            )
            for x, y in points
        ]


print(Solution().count_rectangles([[7, 1], [2, 6], [1, 4], [5, 2], [10, 3], [2, 4], [
      5, 9]], [[10, 3], [8, 10], [2, 3], [5, 4], [8, 5], [7, 10], [6, 6], [3, 6]]))
