"""
https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
"""


from collections import Counter
from functools import reduce
from operator import mul


class Solution:
    """
    Solution
    """

    def beautiful_subsets(self, nums: list[int], k: int) -> int:
        """
        dp(x) returns results for sequence no bigger than x:
            dp(x)[0] is the number of ways without x
            dp(x)[1] is the number of ways with x

        So for dp(x + k) we have:
            dp(x + k)[0] = dp(x)[0] + dp(x)[1]
            dp(x + k)[1] = dp(x)[0] * (2 ** cnt[x + k] - 1)
        """
        def dp(x: int):
            if x - k in cnt:
                dp0, dp1 = dp(x - k)
            else:
                dp0, dp1 = 1, 0

            return (
                dp0 + dp1,
                dp0 * ((1 << cnt[x]) - 1)
            )

        cnt = Counter(nums)
        return reduce(
            mul,
            [
                sum(dp(x))
                for x in cnt
                if not x + k in cnt
            ]
        ) - 1


print(Solution().beautiful_subsets([2, 4, 6], 2))
