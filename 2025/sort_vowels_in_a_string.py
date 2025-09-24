"""
https://leetcode.com/problems/sort-vowels-in-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def sort_vowels(self, s: str) -> str:
        """
        sort vowels
        """
        vowel_set = set('aeiouAEIOU')
        vowels = [c for c in s if c in vowel_set]
        if not vowels:
            return s

        vowels.sort()
        i = 0
        chars = list(s)
        for j, c in enumerate(chars):
            if c in vowel_set:
                chars[j] = vowels[i]
                i += 1

        return ''.join(chars)
