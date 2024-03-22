"""
https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/description/
"""


class Solution:
    """
    Solution
    """

    def min_moves_to_make_palindrome(self, s: str) -> int:
        """
        min moves to make palindrome
        """
        chars = list(s)
        swaps = 0
        while chars:
            i = chars.index(chars[-1])
            if i == len(chars) - 1:
                # Only one occurrence, put it to the middle.
                swaps += len(chars) >> 1
            else:
                # Find a pair, put it to the front of the list.
                swaps += i
                chars.pop(i)

            chars.pop()

        return swaps
