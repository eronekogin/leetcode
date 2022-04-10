"""
https://leetcode.com/problems/distinct-echo-substrings/
"""


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        candidates = set()
        for windowLen in range(1, (N >> 1) + 1):
            l, r = 0, windowLen
            equalChars = 0
            while l < N - windowLen:
                if text[l] == text[r]:
                    equalChars += 1
                else:
                    equalChars = 0

                if equalChars == windowLen:  # Found a candidate.
                    candidates.add(text[l - windowLen + 1: l + 1])
                    equalChars -= 1  # Don't count the current char.

                l, r = l + 1, r + 1

        return len(candidates)
