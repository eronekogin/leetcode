"""
https://leetcode.com/problems/apple-redistribution-into-boxes/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_boxes(self, apple: list[int], capacity: list[int]) -> int:
        """
        minimum boxes
        """
        total_apples = sum(apple)
        boxes = 0
        for c in sorted(capacity, reverse=True):
            total_apples -= c
            boxes += 1
            if total_apples <= 0:
                break

        return boxes
