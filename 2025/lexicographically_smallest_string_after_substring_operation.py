"""
https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_string(self, s: str) -> str:
        """
        smallest string
        """
        chars = list(s) + ['a']
        is_operated = False
        previous_a = -1
        for i, c in enumerate(chars):
            if c == 'a':
                if i > 0:
                    for j in range(previous_a + 1, i):
                        is_operated = True
                        chars[j] = chr(ord(chars[j]) - 1)

                    if is_operated:
                        break

                    previous_a = i
                else:
                    previous_a = 0

        if not is_operated:
            chars[-2] = 'z'

        return ''.join(chars[:-1])
