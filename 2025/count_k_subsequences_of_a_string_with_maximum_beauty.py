"""
https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/description/
"""


from collections import Counter
from functools import reduce
from heapq import nlargest
from math import comb
from operator import mul


class Solution:
    """
    Solution
    """

    def count_k_subsequences_with_max_beauty(self, s: str, k: int) -> int:
        """
        count k subsequences with max beauty
        """
        freqs = Counter(s)
        if len(freqs) < k:
            return 0

        values = list(freqs.values())
        topk = nlargest(k, values)
        limit = topk[-1]

        return (
            reduce(mul, topk) *
            comb(
                values.count(limit),
                topk.count(limit)
            )
        ) % (10 ** 9 + 7)


print(Solution().count_k_subsequences_with_max_beauty('bsacbeqtgw', 6))
