"""
https://leetcode.com/problems/longest-ideal-subsequence/description/
"""


class Solution:
    """
    Solution
    """

    def longest_ideal_string(self, s: str, k: int) -> int:
        """
        longest ideal string
        """
        dp = [0] * 26
        offset = ord('a')
        for i in map(lambda x: ord(x) - offset, s):
            dp[i] = 1 + max(dp[max(0, i - k): min(25, i + k) + 1])

        return max(dp)


print(Solution().longest_ideal_string('pvjcci', 4))
