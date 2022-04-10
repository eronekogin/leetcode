"""
https://leetcode.com/problems/4sum-ii/
"""


from typing import List
from collections import Counter


class Solution:
    def fourSumCount(
            self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        memo = Counter(a + b for a in A for b in B)
        return sum(memo[-c-d] for c in C for d in D)
