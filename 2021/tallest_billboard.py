"""
https://leetcode.com/problems/tallest-billboard/
"""


class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        # dp[d] stands for the maximum pair of sum (a, b) we could get with
        # b - a = d. Then if dp[diff] = a, it means we have a maximum pair of
        # sum (a, a + diff).
        dp = {0: 0}
        for x in rods:
            for d, y in dp.copy().items():
                """
                0. init state 
                    ------|----- d -----|      # tall side 
                    - y --|                    # low  side
                """
                """
                1. put x to tall side:
                    ------|----- d -----|---- x --|
                    - y --|
                """
                dp[d + x] = max(dp.get(x + d, 0), y)

                """
                2.1 Put x to low side and d >= x:
                    -------y------|----- d -----|
                    -------y------|--- x ---|
                    dp[d-x] = max(dp[d - x], y + x)

                2.2 Put x to low side and d < x:
                    ------- y ------|----- d -----|
                    ------- y ------|------- x -------|
                    dp[x - d] = max(dp[x - d], y + d)
                """
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))

        return dp[0]
