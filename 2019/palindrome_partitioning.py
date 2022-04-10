"""
https://leetcode.com/problems/palindrome-partitioning/
"""


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        dp[i] stands for all the partitions made by s[:i + 1].

        dp[i + 1] = [
            p + [s[k: i + 1]]
            for k in range(i + 1)  # Cut at any position.
            for p in dp[k]
            if s[k: i + 1] = s[k: i + 1][::-1]]  # If current cut is palindrome.
        """
        if not s:  # Empty string.
            return [[]]

        n = len(s) + 1
        dp = [[] for _ in range(n)]
        dp[0], dp[1] = [[]], [[s[0]]]
        for i in range(2, n):
            for k in range(i):
                currStr = s[k: i]
                if currStr == currStr[::-1]:
                    dp[i] += [p + [currStr] for p in dp[k]]

        return dp[-1]


s = 'abb'
print(Solution().partition(s))
