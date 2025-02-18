"""
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
"""


class Solution:
    """
    Solution
    """

    def take_characters(self, s: str, k: int) -> int:
        """
        take characters
        """
        if k == 0:
            return 0

        limits = {c: s.count(c) - k for c in 'abc'}
        if any(v < 0 for v in limits.values()):
            return -1

        cnt = {c: 0 for c in 'abc'}
        max_window = start = 0
        for end, c in enumerate(s):
            cnt[c] += 1

            while cnt[c] > limits[c]:
                cnt[s[start]] -= 1
                start += 1

            max_window = max(max_window, end - start + 1)

        return len(s) - max_window
