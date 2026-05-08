"""
https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/
"""


from itertools import combinations


class Solution:
    """
    Solution
    """

    def largest_square_area(self, bottom_left: list[list[int]], top_right: list[list[int]]) -> int:
        """
        largest square area
        """
        max_size = 0

        for (bl1, tr1), (bl2, tr2) in combinations(zip(bottom_left, top_right), 2):
            w = min(tr1[0], tr2[0]) - max(bl1[0], bl2[0])
            h = min(tr1[1], tr2[1]) - max(bl1[1], bl2[1])
            max_size = max(max_size, min(w, h))

        return max_size ** 2
