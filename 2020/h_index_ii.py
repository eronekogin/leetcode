"""
https://leetcode.com/problems/h-index-ii/
"""


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Since the citations are pre-sorted, we could use binary search
        to accelerate the process.

        Presumption: the input citations are sorted in ascending order.
        """
        l = 0
        r = n = len(citations)
        while l < r:
            m = (l + r) >> 1
            if n - m == citations[m]:
                return n - m
            elif n - m > citations[m]:
                l = m + 1
            else:
                r = m

        return n - l


print(Solution().hIndex([0, 1, 3, 5, 6]))
