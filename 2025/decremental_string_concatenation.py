"""
https://leetcode.com/problems/decremental-string-concatenation/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def minimize_concatenated_length(self, words: list[str]) -> int:
        """
        minimize concatenated length
        """
        @cache
        def reduced_chars(prev_start: str, prev_end: str, curr_index: int) -> int:
            if curr_index == n:
                return 0

            curr_start = words[curr_index][0]
            curr_end = words[curr_index][-1]

            return max(
                (curr_start == prev_end) +
                reduced_chars(prev_start, curr_end, curr_index + 1),
                (prev_start == curr_end) +
                reduced_chars(curr_start, prev_end, curr_index + 1)
            )

        n = len(words)
        return sum(map(len, words)) - reduced_chars(words[0][0], words[0][-1], 1)
