"""
https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def shortest_beautiful_substring(self, s: str, k: int) -> str:
        """
        Docstring for shortest_beautiful_substring

        :param self: Description
        :param s: Description
        :type s: str
        :param k: Description
        :type k: int
        :return: Description
        :rtype: str
        """
        ones = [i for i, c in enumerate(s) if c == '1']
        curr_min = len(s) + 1
        curr_str = '1' * len(s)
        for a, b in zip(ones, ones[k - 1:]):
            if b - a < curr_min:
                curr_min = b - a
                curr_str = s[a: b + 1]
            elif b - a == curr_min:
                if s[a: b + 1] < curr_str:
                    curr_str = s[a: b + 1]

        if curr_min == len(s) + 1:
            return ''

        return curr_str
