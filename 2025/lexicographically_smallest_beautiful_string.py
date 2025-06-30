"""
https://leetcode.com/problems/lexicographically-smallest-beautiful-string/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_beautiful_string(self, s: str, k: int) -> str:
        """
        smallest beautiful string
        """
        n = len(s)
        base = ord('a')
        digits = [ord(c) - base for c in s]
        i = n - 1
        while i >= 0:
            digits[i] += 1

            if digits[i] == k:
                i -= 1
            elif digits[i] not in digits[max(i - 2, 0): i]:
                for j in range(i + 1, n):
                    digits[j] = min({0, 1, 2} - set(digits[max(0, j - 2): j]))

                return ''.join(chr(base + d) for d in digits)

        return ''
