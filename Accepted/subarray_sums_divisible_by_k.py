"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/
"""


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        1. Suppose b is the current total, while a is the previous total,
            then if the sum between a and b is divisible by k, we have:
            b - a = n * k, then b = a + n * k -> b % k = a % k.
        2. So if we found if the current sum % k has the same value as
            previous sums, we could know that the subarray between a and b
            is a candidate.
        """
        counters = [1] + [0] * k  # The first 1 stands for an empty array.
        rslt = prefixSum = 0
        for num in nums:
            prefixSum = (prefixSum + num) % k
            rslt += counters[prefixSum]
            counters[prefixSum] += 1

        return rslt
