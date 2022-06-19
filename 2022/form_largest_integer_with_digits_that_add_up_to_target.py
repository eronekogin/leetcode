"""
https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
"""


class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        # target or cost[i] is <= 5000, here just make sure t - c is not out
        # of index of dp list.
        dp = [0] + [-1] * (target + 5000)

        # Insert the next digit at end since the previous result is already
        # maximized.
        for t in range(1, target + 1):
            dp[t] = max(
                dp[t - c] * 10 + i + 1
                for i, c in enumerate(cost)
            )

        return str(max(dp[t], 0))
