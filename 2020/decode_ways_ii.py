"""
https://leetcode.com/problems/decode-ways-ii/
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        prev = 1  # Initially selecting zero char.

        # Initially selecting one char.
        if s[0] == '*':  # [1, 9]
            curr = 9
        elif s[0] == '0':  # Single zero cannot be decoded.
            curr = 0
        else:  # Match to any number in [1, 9].
            curr = 1

        for i in range(1, len(s)):
            temp = curr
            if s[i] == '*':
                curr *= 9  # When taking the s[i] separately
                if s[i - 1] == '1':  # Case 1*: [11, 19]
                    curr += 9 * prev
                elif s[i - 1] == '2':  # Case 2*: [21, 26]
                    curr += 6 * prev
                elif s[i - 1] == '*':  # Either 1* or 2*
                    curr += 15 * prev
            else:
                if s[i] == '0':  # When taking the s[i] separately
                    curr = 0

                if s[i - 1] == '1':  # Case 1x: [10, 19]
                    curr += prev
                elif s[i - 1] == '2' and int(s[i]) <= 6:  # Case 2x: [20, 26]
                    curr += prev
                elif s[i - 1] == '*':  # Case *x
                    if int(s[i]) <= 6:  # [10, 16] or [20, 26]
                        curr += 2 * prev
                    else:  # [17, 19]
                        curr += prev

            prev = temp

        return curr % (10 ** 9 + 7)
