"""
https://leetcode.com/problems/lexicographically-smallest-palindrome/description/
"""


class Solution:
    """
    Solution
    """

    def make_smallest_palindrome(self, s: str) -> str:
        """
        make smallest paldinrome
        """
        l, r = 0, len(s) - 1
        rslt = list(s)
        while l <= r:
            lc, rc = rslt[l], rslt[r]
            if lc < rc:
                rslt[r] = rslt[l]
            else:
                rslt[l] = rslt[r]

            l += 1
            r -= 1

        return ''.join(rslt)
