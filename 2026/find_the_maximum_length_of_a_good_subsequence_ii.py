"""
https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def maximum_length(self, nums: list[int], k: int) -> int:
        """
        maximum length
        """
        good_sequences = [0] * (k + 1)
        dp = [defaultdict(int) for _ in range(k + 1)]

        for x in nums:
            for i in range(k, -1, -1):
                dp[i][x] = max(
                    dp[i][x] + 1,
                    good_sequences[i - 1] + 1 if i > 0 else 0
                )
                good_sequences[i] = max(
                    good_sequences[i],
                    dp[i][x]
                )

        return good_sequences[-1]
