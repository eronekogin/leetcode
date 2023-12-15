"""
https://leetcode.com/problems/two-furthest-houses-with-different-colors/
"""


class Solution:
    """
    Solution
    """

    def max_distance(self, colors: list[int]) -> int:
        """
        max_distance
        """
        i, j = 0, len(colors) - 1
        while colors[0] == colors[j]:
            j -= 1
        while colors[-1] == colors[i]:
            i += 1
        return max(len(colors) - 1 - i, j)
