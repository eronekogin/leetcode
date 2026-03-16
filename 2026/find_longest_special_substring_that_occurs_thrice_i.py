"""
https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/
"""


from collections import Counter
from itertools import groupby


class Solution:
    """
    Solution
    """

    def maximum_length(self, s: str) -> int:
        """
        maximum length
        """
        cnt = Counter()

        for _, gp in groupby(s):
            sub = ''.join(gp)

            cnt[sub] += 1
            if len(sub) > 1:
                cnt[sub[1:]] += 2

            if len(sub) > 2:
                cnt[sub[2:]] += 3

        return max(
            [len(k) for k, v in cnt.items() if v >= 3],
            default=-1
        )
