"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        BASE = ord('a')
        memo: list[list[int | None]] = [[None, None] for _ in range(26)]
        for i, c in enumerate(s):
            offset = ord(c) - BASE
            if memo[offset][0] is None:
                memo[offset][0] = i
            else:
                memo[offset][1] = i

        return max(
            [
                end - start - 1
                for start, end in memo
                if start is not None and end is not None
            ] or [-1]
        )
