"""
https://leetcode.com/problems/find-the-encrypted-string/description/
"""


class Solution:
    """
    Solution
    """

    def get_encrypted_string(self, s: str, k: int) -> str:
        """
        get encrypted string
        """
        chars = list(s)
        n = len(s)

        for i in range(n):
            chars[i] = s[(i + k) % n]

        return ''.join(chars)
