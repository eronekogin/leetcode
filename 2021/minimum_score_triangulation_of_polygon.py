"""
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
"""


class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        """
        1. For vector i and vector j, any vector k between i and j could form
            a triangle and those triangles share the same edge which connects
            i and j.
        2. The mininum value between i and j are the minimum value among the
            above triangles.
        """
        def dp(start: int, end: int) -> int:
            if (start, end) not in memo:
                memo[(start, end)] = min(
                    [
                        dp(start, mid) + dp(mid, end) +
                        values[start] * values[end] * values[mid]
                        for mid in range(start + 1, end)
                    ] or [0]
                )

            return memo[(start, end)]

        memo = {}
        return dp(0, len(values) - 1)
