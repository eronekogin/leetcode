"""
https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description/
"""

from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def min_absolute_difference(self, nums: list[int], x: int) -> int:
        """
        min absolute difference
        """
        sorted_nums = sorted((y, i) for i, y in enumerate(nums))
        left_heap: list[tuple[int, int]] = []
        right_heap: list[tuple[int, int]] = []

        rslt = 10 ** 9 + 1

        for y, i in sorted_nums:
            heappush(left_heap, (i, y))
            heappush(right_heap, (-i, y))

            while left_heap and left_heap[0][0] + x <= i:
                rslt = min(rslt, y - heappop(left_heap)[1])

            while right_heap and right_heap[0][0] + x <= -i:
                rslt = min(rslt, y - heappop(right_heap)[1])

        return rslt
