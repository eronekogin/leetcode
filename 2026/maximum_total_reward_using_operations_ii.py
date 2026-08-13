"""
https://leetcode.com/problems/maximum-total-reward-using-operations-ii/description/
"""


from bisect import bisect_left
from functools import cache


class Solution:
    """
    Solution
    """

    def max_total_reward(self, reward_values: list[int]) -> int:
        """
        max total reward
        """
        @cache
        def check(x: int) -> int:
            i = bisect_left(vals, x) - 1
            if i < 0:
                return 0

            rslt = -1
            while i >= 0:
                if vals[i] <= x // 2:
                    rslt = max(rslt, vals[i] + check(vals[i]))
                    break

                rslt = max(rslt, vals[i] + check(x - vals[i]))
                if rslt + 1 == x:
                    break

                i -= 1

            return rslt

        vals = sorted(set(reward_values))
        return vals[-1] + check(vals[-1])
