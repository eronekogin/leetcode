"""
https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/
"""


class Solution:
    """
    Solution
    """

    def count_k_constraint_substrings(self, s: str, k: int) -> int:
        """
        count k constraint substrings
        """
        rslt = 0
        ones = 0
        start = 0

        for end, c in enumerate(s):
            ones += c == '1'

            while ones > k and end - start + 1 - ones > k:
                ones -= s[start] == '1'
                start += 1

            rslt += end - start + 1

        return rslt
