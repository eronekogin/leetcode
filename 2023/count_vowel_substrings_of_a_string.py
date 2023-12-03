"""
https://leetcode.com/problems/count-vowel-substrings-of-a-string/
"""


class Solution:
    """
    Solution
    """

    def count_vowel_substrings(self, word: str) -> int:
        """
        count_vowel_substrings
        """
        rslt = 0
        last_consonant = -1
        last_seen_vowels = {c: -1 for c in 'aeiou'}

        for i, c in enumerate(word):
            if c in last_seen_vowels:
                last_seen_vowels[c] = i
                rslt += max(min(last_seen_vowels.values()) - last_consonant, 0)
            else:
                last_consonant = i

        return rslt
