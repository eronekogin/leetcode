"""
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
"""


class Solution:
    def minOperations(self, s: str) -> int:
        # To make string 01010101...0101, we need the following actions.
        cnt = sum(i % 2 == int(c) for i, c in enumerate(s))

        # To make string 10101010...1010, we need len(s) - cnt actions.

        # So the result will be the minimum between the above two actions.
        return min(cnt, len(s) - cnt)
