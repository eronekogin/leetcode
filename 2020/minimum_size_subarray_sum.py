"""
https://leetcode.com/problems/minimum-size-subarray-sum/
"""


from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        start, subSum, minLen = 0, 0, n + 1
        for end, num in enumerate(nums):
            subSum += num
            while subSum >= s:
                minLen = min(minLen, end - start + 1)
                subSum -= nums[start]
                start += 1

        if minLen == n + 1:
            return 0

        return minLen


s = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(s, nums))
