"""
https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_number_of_string_pairs(self, words: list[str]) -> int:
        """
        maximum number of string pairs
        """
        pairs = 0
        memo = set(words)
        for w in words:
            pw = w[::-1]
            if pw != w and pw in memo:
                pairs += 1

        return pairs >> 1
