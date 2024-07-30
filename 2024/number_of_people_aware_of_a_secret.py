"""
https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/
"""


class Solution:
    """
    Solution
    """

    def people_aware_of_secret(self, n: int, delay: int, forget: int) -> int:
        """
        Suppose dp[i] stands for the number of people who found the secret
        on the ith day:

            * On the ith day, dp[i - delay] people starts to share secret
            * On the ith day, dp[i - forget] people forgot the secret
        """
        m = 10 ** 9 + 7
        dp = [1] + [0] * (n - 1)
        share = 0

        for i in range(1, n):
            dp[i] = share = (share + dp[i - delay] - dp[i - forget]) % m

        return sum(dp[-forget:]) % m


print(Solution().people_aware_of_secret(6, 2, 4))
