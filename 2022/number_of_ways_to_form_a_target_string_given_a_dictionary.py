"""
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
"""


from collections import Counter


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        N, MOD = len(target), 10 ** 9 + 7

        # The number of ways to form the first j chars in target.
        dp = [1] + [0] * N

        for i in range(len(words[0])):
            cnt = Counter(w[i] for w in words)
            for j in range(N - 1, -1, -1):
                dp[j + 1] += dp[j] * cnt[target[j]] % MOD

        return dp[N] % MOD
