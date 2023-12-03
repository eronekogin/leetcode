"""
https://leetcode.com/problems/vowels-of-all-substrings/
"""


class Solution:
    """
    Solution
    """

    def count_vowels(self, word: str) -> int:
        """
        Suppose s[i] is a vowel, then it could occur in any substring starting at s[x] and
        ending at s[y], while 0 <= x <= i and i <= y <= len(word), so there is (i + 1) choices
        for x and len(word) - i choices for y, which means there are (i + 1) * (len(word) - i)
        substrings that contains s[i].
        """
        return sum(
            (i + 1) * (len(word) - i)
            for i, c in enumerate(word)
            if c in 'aeiou'
        )


print(Solution().count_vowels('aba'))
