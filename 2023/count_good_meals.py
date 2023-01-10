"""
https://leetcode.com/problems/count-good-meals/
"""


from collections import defaultdict


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        freqs = defaultdict(int)
        pairs = 0
        for x in deliciousness:
            for i in range(22):
                pairs += freqs[(1 << i) - x]

            freqs[x] += 1

        return pairs % (10 ** 9 + 7)
