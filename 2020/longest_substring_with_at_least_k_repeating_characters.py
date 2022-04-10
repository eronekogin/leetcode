"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""


from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) < k:
            return 0

        if k == 1:
            return len(s)

        for c, total in Counter(s).items():
            if total < k:
                # When the total occurrences of c is less than k, it means
                # any sub string containing c will not satisfy.
                return max([self.longestSubstring(t, k) for t in s.split(c)])

        return len(s)  # All the characters in s satisfy.
