"""
https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/
"""


class Solution:
    """
    Solution
    """

    def smallest_sub_sequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        """
        smallest_sub_sequence
        """
        remain_letters = sum(c == letter for c in s)
        stack = []
        n = len(s)

        for i, c in enumerate(s):
            while (
                stack and
                stack[-1] > c and
                n - i + len(stack) > k and
                (stack[-1] != letter or remain_letters > repetition)
            ):
                d = stack.pop()
                if d == letter:
                    repetition += 1

            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    repetition -= 1
                elif k > repetition + len(stack):
                    stack.append(c)

            if c == letter:
                remain_letters -= 1

        return ''.join(stack)
