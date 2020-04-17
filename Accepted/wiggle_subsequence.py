"""
https://leetcode.com/problems/wiggle-subsequence/
"""


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        preAscending = None
        maxWiggleLen = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:  # Ascending.
                if preAscending is None or not preAscending:
                    preAscending = True
                    maxWiggleLen += 1
            elif nums[i] < nums[i - 1]:  # Descending.
                if preAscending is None or preAscending:
                    preAscending = False
                    maxWiggleLen += 1

        return maxWiggleLen


print(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
