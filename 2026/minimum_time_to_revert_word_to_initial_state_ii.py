"""
https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_time_to_initial_state(self, word: str, k: int) -> int:
        """
        minimum time to initial state
        """
        n = len(word)
        dp = [0] * n
        v = 0

        # KMP
        for i in range(1, n):
            while v and word[i] != word[v]:
                v = dp[v - 1]

            v = dp[i] = v + (word[i] == word[v])

        while v and (n - v) % k > 0:
            v = dp[v - 1]

        return (n - v + k - 1) // k
