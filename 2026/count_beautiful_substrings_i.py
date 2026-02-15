"""
https://leetcode.com/problems/count-beautiful-substrings-i/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def beautiful_substrings(self, s: str, k: int) -> int:
        """
        Docstring for beautiful_substrings

        :param self: Description
        :param s: Description
        :type s: str
        :param k: Description
        :type k: int
        :return: Description
        :rtype: int
        """
        cnt = 0
        n = len(s)
        for start in range(n):
            c = v = 0
            for end in range(start, n):
                if s[end] in 'aeiou':
                    v += 1
                else:
                    c += 1

                if v == c and (v * v) % k == 0:
                    cnt += 1

        return cnt


print(Solution().beautiful_substrings('baeyh', 2))
