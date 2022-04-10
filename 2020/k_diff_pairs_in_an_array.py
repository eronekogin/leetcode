"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""


from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:  # Absolute difference is always non-negative.
            return 0

        c = Counter(nums)
        if k == 0:
            return sum(v > 1 for v in c.values())

        return sum(num + k in c for num in c)  # When k > 0.


print(Solution().findPairs([6, 3, 5, 7, 2, 3, 3, 8, 2, 4], 2))
