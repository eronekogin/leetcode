"""
https://leetcode.com/problems/valid-word/description/
"""


class Solution:
    """
    Solution
    """

    def is_valid(self, word: str) -> bool:
        """
        is valid
        """
        if len(word) < 3:
            return False

        if not word.isalnum():
            return False

        vowels = 'aeiou'
        has_vowel = has_consonant = False

        for c in word:
            if c.lower() in vowels:
                has_vowel = True
            elif not c.isdigit():
                has_consonant = True

            if has_vowel and has_consonant:
                break

        return has_vowel and has_consonant
