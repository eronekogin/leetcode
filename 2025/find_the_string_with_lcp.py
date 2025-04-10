"""
https://leetcode.com/problems/find-the-string-with-lcp/description/
"""


class Solution:
    """
    Solution
    """

    def find_the_string(self, lcp: list[list[int]]) -> str:
        """
        If lcp[i][j] > 0, then A[i] = A[j], else A[i] != A[j]
        """
        n = len(lcp)
        chars = [0] * n
        curr = 1

        for i in range(n):
            if chars[i]:
                continue

            if curr > 26:  # No more chars to be used
                return ''

            for j in range(i, n):
                if lcp[i][j]:  # Have common prefix
                    chars[j] = curr

            curr += 1

        for i in range(n):
            for j in range(n):
                if i + 1 < n and j + 1 < n:
                    t = lcp[i + 1][j + 1]
                else:
                    t = 0

                if chars[i] == chars[j]:
                    t += 1
                else:
                    t = 0

                if lcp[i][j] != t:
                    return ''

        return ''.join(chr(ord('a') + i - 1) for i in chars)
