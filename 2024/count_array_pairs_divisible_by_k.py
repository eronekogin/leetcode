"""
https://leetcode.com/problems/count-array-pairs-divisible-by-k/description/
"""


from math import gcd
from collections import Counter


class Solution:
    """
    Solution
    """

    def count_pairs(self, nums: list[int], k: int) -> int:
        """
        if a * b % k == 0, then gcd(a, k) * gcd(b, k) % k == 0.
        """
        pairs = 0
        gcd_cnt = Counter(gcd(x, k) for x in nums)
        for a in gcd_cnt:
            for b in gcd_cnt:
                if a <= b and a * b % k == 0:
                    if a < b:
                        pairs += gcd_cnt[a] * gcd_cnt[b]
                    else:
                        pairs += (gcd_cnt[a] * (gcd_cnt[a] - 1)) >> 1

        return pairs
