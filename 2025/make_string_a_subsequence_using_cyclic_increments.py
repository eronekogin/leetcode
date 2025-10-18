"""
https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/
"""


class Solution:
    """
    Solution
    """

    def can_make_subsequence(self, str1: str, str2: str) -> bool:
        """
        can make subsequence
        """
        if len(str2) > len(str1):
            return False

        i = 0
        n = len(str1)
        base = ord('a')
        for c in str2:
            p = chr(((ord(c) - base - 1) % 26) + base)
            while i < n and str1[i] != c and str1[i] != p:
                i += 1

            if i == n:
                return False

            i += 1

        return True


print(Solution().can_make_subsequence('abc', 'abcd'))
