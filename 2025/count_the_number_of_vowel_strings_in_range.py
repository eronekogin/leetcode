"""
https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/
"""


class Solution:
    """
    Solution
    """

    def vowel_strings(self, words: list[str], left: int, right: int) -> int:
        """
        vowel strings
        """
        return sum(
            s[0] in 'aeiou' and s[-1] in 'aeiou'
            for s in words[left: right + 1]
        )
