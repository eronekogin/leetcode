"""
https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """
    def max_score(self, grid: list[list[int]]) -> int:
        """
        max score
        """
        val_to_rows = defaultdict(set)
        for r, row in enumerate(grid):
            for v in row:
                val_to_rows[v].add(r)

        unique_nums = sorted(val_to_rows.keys(), reverse=True)
        m = len(grid)

        dp = [0] * (1 << m)

        for v in unique_nums:
            rows = val_to_rows[v]
            new_dp = list(dp)

            for mask in range(1 << m):
                if dp[mask] > 0 or mask == 0:
                    for r in rows:
                        if not mask & (1 << r):
                            new_dp[mask | (1 << r)] = max(
                                new_dp[mask | (1 << r)],
                                dp[mask] + v
                            )

            dp = new_dp

        return max(dp)
