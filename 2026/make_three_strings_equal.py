"""
https://leetcode.com/problems/make-three-strings-equal/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_minimum_operations(self, s1: str, s2: str, s3: str) -> int:
        """
        Docstring for find_minimum_operations

        :param self: Description
        :param s1: Description
        :type s1: str
        :param s2: Description
        :type s2: str
        :param s3: Description
        :type s3: str
        :return: Description
        :rtype: int
        """
        n = min(len(s1), len(s2), len(s3))
        i = 0
        while i < n:
            if s1[i] == s2[i] == s3[i]:
                i += 1
            else:
                break

        if i > 0:
            return len(s1) + len(s2) + len(s3) - 3 * i

        return -1


print(Solution().find_minimum_operations('abc', 'abb', 'ab'))
