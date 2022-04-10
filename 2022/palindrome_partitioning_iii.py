"""
https://leetcode.com/problems/palindrome-partitioning-iii/
"""


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def dfs(s: str, k: int) -> int:
            if (s, k) not in memo:
                if len(s) == k:
                    return 0  # Takes zero change.

                if k == 1:
                    res = sum(s[i] != s[-1-i] for i in range(len(s) >> 1))
                else:
                    res = float('inf')
                    for i in range(1, len(s) - k + 2):
                        res = min(
                            res,
                            dfs(s[:i], 1) + dfs(s[i:], k - 1)
                        )

                memo[(s, k)] = res

            return memo[(s, k)]

        memo = {}
        return dfs(s, k)
