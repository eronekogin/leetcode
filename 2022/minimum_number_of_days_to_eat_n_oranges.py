"""
https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/
"""


from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        """
        dp returns the minimum number of days to eat remainingOranges oranges.
        """
        @lru_cache(None)
        def dp(remainOranges: int) -> int:
            if remainOranges <= 1:
                return 1

            return 1 + min(
                remainOranges % 2 + dp(remainOranges // 2),
                remainOranges % 3 + dp(remainOranges // 3)
            )

        return dp(n)


print(Solution().minDays(10))
