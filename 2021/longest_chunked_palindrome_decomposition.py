"""
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
"""


class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        1. shorter match could always break more sub groups than longer match.
        2. For any longer match, it contains the following patterns:
            2.1 shorter = a + bc * (N - 1), longer = a + bc * N
            2.2 shoter = bc * N, longer = bc * M where M > N
        """
        N = len(text)
        cnt, l, r = 0, '', ''
        for i in range(N >> 1):
            l, r = l + text[i], text[N - 1 - i] + r
            if l == r:
                cnt, l, r = cnt + 2, '', ''

        if not N & 1 and not l and not r:
            return cnt

        return cnt + 1  # Has a last remaining middle part


print(Solution().longestDecomposition("elvtoelvto"))
