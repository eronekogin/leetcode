"""
https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_special_chars(self, word: str) -> int:
        """
        number of special chars
        """
        lower_cases = [0] * 26
        upper_cases = [0] * 26
        o1 = ord('a')
        o2 = ord('A')
        for w in map(ord, word):
            if w >= o1:
                lower_cases[w - o1] = 1
            else:
                upper_cases[w - o2] = 1

        return sum(l > 0 and r > 0 for l, r in zip(lower_cases, upper_cases))
