"""
https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/description/
"""


class Solution:
    """
    Solution
    """

    def capture_forts(self, forts: list[int]) -> int:
        """
        capture forts
        """
        max_captured = 0
        start = 0
        n = len(forts)
        while start < n and forts[start] == 0:
            start += 1

        end = start + 1
        while end < n:
            while end < n and forts[end] == 0:
                end += 1

            if end < n and (
                (forts[start] == 1 and forts[end] == -1) or
                (forts[start] == -1 and forts[end] == 1)
            ):
                max_captured = max(max_captured, end - start - 1)

            start = end
            end += 1

        return max_captured
