"""
https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/description/
"""


class Solution:
    """
    Solution
    """

    def longest_subsequence(self, s: str, k: int) -> int:
        """
        longest subsequence
        """
        cnt = 0
        curr = 0
        for c in reversed(s):
            x = int(c)
            if curr + (x << cnt) > k:
                continue

            curr += (x << cnt)
            cnt += 1

        return cnt


print(Solution().longest_subsequence('1001010', 5))
