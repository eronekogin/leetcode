"""
https://leetcode.com/problems/minimum-length-of-string-after-operations/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_length(self, s: str) -> int:
        """
        minimum length
        """
        cnt = Counter(s)
        rslt = 0
        for v in cnt.values():
            rslt += 1 + (v & 1 == 0)

        return rslt
