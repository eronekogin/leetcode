"""
https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
"""


from collections import Counter
from itertools import combinations


class Solution:
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        def count(nums1: list[int], nums2: list[int]) -> int:
            squareCnt1 = Counter(n1 ** 2 for n1 in nums1)
            return sum(squareCnt1[x * y] for x, y in combinations(nums2, 2))

        return count(nums1, nums2) + count(nums2, nums1)


print(Solution().numTriplets([7, 4],
                             [5, 2, 8, 9]))
