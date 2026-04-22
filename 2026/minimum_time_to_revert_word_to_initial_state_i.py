"""
https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_time_to_initial_state(self, word: str, k: int) -> int:
        """
        * Find the longest prefix that ends at the end of the word, for example:
            abcdxxxabcd, longest prefix is abcd.

        * Suppose the length of the prefix is v, then check if (n - v) % k == 0,
            if so, we can use ceil((n - v) / k) operations to achieve the goal.

        * If (n - v) % k > 0, we check the next longest prefix which would be
            dp[v - 1] instead.
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
