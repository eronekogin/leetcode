"""
https://leetcode.com/problems/maximum-multiplication-score/description/
"""


from math import inf


class Solution:
    """
    Solution
    """

    def max_score(self, a: list[int], b: list[int]) -> int:
        """
        max score
        """
        dp0 = dp1 = dp2 = dp3 = -inf

        for y in b:
            dp3 = max(dp3, dp2 + a[3] * y)
            dp2 = max(dp2, dp1 + a[2] * y)
            dp1 = max(dp1, dp0 + a[1] * y)
            dp0 = max(dp0, a[0] * y)

        return int(dp3)
