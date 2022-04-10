"""
https://leetcode.com/problems/shifting-letters/
"""


class Solution:
    def shiftingLetters(self, S: str, shifts: list[int]) -> str:
        CHARS = 'abcdefghijklmnopqrstuvwxyz'
        MEMO = {c: i for i, c in enumerate(CHARS)}
        offsets = [sum(shifts)]
        for i in range(1, len(shifts)):
            offsets.append(offsets[-1] - shifts[i - 1])

        return ''.join(
            CHARS[(MEMO[c] + offsets[i]) % 26] for i, c in enumerate(S))


print(Solution().shiftingLetters('abc', [3, 5, 9]))
