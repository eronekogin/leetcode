"""
https://leetcode.com/problems/make-sum-divisible-by-p/
"""


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        needRemainder = sum(nums) % p

        minLen = N = len(nums)
        prefixSum = 0
        memo = {0: -1}  # Record the rightmost index of prefixSum % p
        for i, num in enumerate(nums):
            prefixSum = (prefixSum + num) % p
            memo[prefixSum] = i

            prevRemainder = (prefixSum - needRemainder) % p
            if prevRemainder in memo:
                minLen = min(minLen, i - memo[prevRemainder])

        if minLen < N:
            return minLen

        return -1  # Not possible.


print(Solution().minSubarray([3, 1, 4, 2], 6))
