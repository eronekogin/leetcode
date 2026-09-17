"""
https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/
"""


class Solution:
    """
    Solution
    """

    def get_smallest_string(self, s: str) -> str:
        """
        get smallest string
        """
        chars = list(s)
        for i, (c1, c2) in enumerate(zip(chars, chars[1:])):
            d1, d2 = int(c1), int(c2)
            if d2 < d1 and d2 & 1 == d1 & 1:
                chars[i] = c2
                chars[i + 1] = c1
                break

        return ''.join(chars)
