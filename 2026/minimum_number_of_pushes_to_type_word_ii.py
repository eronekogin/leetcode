"""
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_pushes(self, word: str) -> int:
        """
        minimum pushes
        """
        cnt = [0] * 26
        offset = ord('a')
        for c in map(ord, word):
            cnt[c - offset] += 1

        cnt.sort(reverse=True)
        pushes = 0

        for i in range(26):
            if cnt[i] == 0:
                break

            pushes += (i // 8 + 1) * cnt[i]

        return pushes
