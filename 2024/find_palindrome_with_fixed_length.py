"""
https://leetcode.com/problems/find-palindrome-with-fixed-length/description/
"""


class Solution:
    """
    Solution
    """

    def kth_palindrome(self, queries: list[int], int_length: int) -> list[int]:
        """
        kth palindrome
        """
        start = 10 ** ((int_length - 1) >> 1)
        rslt = [q - 1 + start for q in queries]
        for i, x in enumerate(rslt):
            s = str(x) + str(x)[-1 - (int_length & 1)::-1]
            if len(s) == int_length:
                rslt[i] = int(s)
            else:
                rslt[i] = -1

        return rslt


print(Solution().kth_palindrome([1, 2, 3, 4, 5, 90], 3))
