"""
https://leetcode.com/problems/assign-cookies/
"""


from typing import List
from collections import Counter


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookies = sorted(s)
        satisfied = 0
        i, n = 0, len(cookies)
        for kid in sorted(g):
            while i < n and cookies[i] < kid:
                i += 1  # Skip the unsatisfied cookies.

            if i == n:
                break

            satisfied += 1
            i += 1

        return satisfied
