"""
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""


from typing import List


from math import ceil


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = l + ((r - l) >> 1)
            currSum = sum(ceil(num / m) for num in nums)
            if currSum > threshold:
                l = m + 1
            else:
                r = m

        return l
