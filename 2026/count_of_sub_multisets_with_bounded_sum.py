"""
https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/description/
"""


from collections import Counter


class Solution:
    """
    Docstring for Solution
    """

    def count_sub_multisets(self, nums: list[int], l: int, r: int) -> int:
        """
        dp[i] is the ways to sum up to i, and the goal is to get
        dp[l] + ... + dp[r]

        Suppose we have c items of number x in nums, then we could iterate i
        from r to 1 and update dp[i] as
            dp[i] = dp[i - x] + dp[i - 2x] + ... + dp[i - cx]
        """
        m = 10 ** 9 + 7
        cnt = Counter(nums)
        dp = [0] * (r + 1)
        dp[0] = 1

        for x, f in cnt.items():
            limit = x * f
            for curr_sum in range(r, max(r - x, 0), -1):
                v = sum(
                    dp[curr_sum - x * k]
                    for k in range(f)
                    if curr_sum >= x * k
                )

                for j in range(curr_sum, 0, -x):
                    v -= dp[j]
                    if j >= limit:
                        v += dp[j - limit]

                    dp[j] = (dp[j] + v) % m

        return (sum(dp[l:]) * (cnt[0] + 1)) % m
