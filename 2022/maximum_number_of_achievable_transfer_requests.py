"""
https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
"""

from itertools import combinations
from collections import Counter


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        """
        Since the total requests is small, which is less than 16, we could
        use brutal force to try to satisfy most requests first to least.
        """
        for satisfied in range(len(requests), -1, -1):
            for comb in combinations(requests, satisfied):
                if Counter(a for a, _ in comb) == Counter(b for _, b in comb):
                    return satisfied

        return 0
