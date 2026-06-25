"""
https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_special_chars(self, word: str) -> int:
        """
        number of special chars
        """
        lower_cases = [-1] * 26
        upper_cases = [-1] * 26
        o1 = ord('a')
        o2 = ord('A')
        for i, w in enumerate(map(ord, word)):
            if w >= o1:
                lower_cases[w - o1] = i
            elif upper_cases[w - o2] < 0:
                upper_cases[w - o2] = i

        return sum(0 <= l < r for l, r in zip(lower_cases, upper_cases))
