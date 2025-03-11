"""
https://leetcode.com/problems/maximum-subsequence-score/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def max_score(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        max score
        """
        total = rslt = 0
        h: list[int] = []

        for a, b in sorted(zip(nums1, nums2), key=lambda x: -x[1]):
            heappush(h, a)
            total += a

            if len(h) > k:
                total -= heappop(h)

            if len(h) == k:
                rslt = max(rslt, total * b)

        return rslt


print(Solution().max_score([1, 3, 3, 2], [2, 1, 3, 4], 3))
