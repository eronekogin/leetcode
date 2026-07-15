"""
https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description/
"""


from collections import Counter
from math import inf


class Solution:
    """
    Solution
    """

    def minimum_substrings_in_partition(self, s: str) -> int:
        """
        minimum substrings in partition
        """
        n = len(s)
        dp = [0] + [inf] * n
        for end in range(n):
            cnt = Counter()
            for start in range(end, -1, -1):
                cnt[s[start]] += 1
                if len(set(cnt.values())) == 1:
                    dp[end + 1] = min(dp[end + 1], dp[start] + 1)

        return int(dp[-1])
