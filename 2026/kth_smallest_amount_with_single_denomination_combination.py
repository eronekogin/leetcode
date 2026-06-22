"""
https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/description/
"""


from collections import defaultdict
from itertools import combinations
from math import lcm


class Solution:
    """
    Solution
    """

    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        """
        find kth smallest
        """
        def count(x: int) -> int:
            cnt = 0

            for i in range(1, n + 1):
                for i_lcm in memo[i]:
                    cnt += x // i_lcm * pow(-1, i + 1)

            return cnt

        n = len(coins)
        memo = defaultdict(list)
        for i in range(1, n + 1):
            for comb in combinations(coins, i):
                memo[len(comb)].append(lcm(*comb))

        l = min(coins)
        r = l * k

        while l + 1 < r:
            m = l + ((r - l) >> 1)
            if count(m) >= k:
                r = m
            else:
                l = m

        if count(l) >= k:
            return l

        return r
