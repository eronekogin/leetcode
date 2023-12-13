"""
https://leetcode.com/problems/decode-the-slanted-ciphertext/
"""


class Solution:
    """
    Solution
    """

    def decode_ciphertext(self, encoded_text: str, rows: int) -> str:
        """
        1. length of encoded_text = rows * cols
        2. s[i]'s adjancent char is s[i + cols + 1].
        """
        total = len(encoded_text)
        cols = total // rows
        chars = []
        for i in range(cols):
            while i < total:
                chars.append(encoded_text[i])
                i += cols + 1

        return ''.join(chars).rstrip()
