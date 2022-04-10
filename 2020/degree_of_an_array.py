"""
https://leetcode.com/problems/degree-of-an-array/
"""


from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        memo, maxFreq, minLen = {}, 0, len(nums) + 1
        for end, num in enumerate(nums):
            if num not in memo:
                memo[num] = [end, 0]

            memo[num][1] += 1
            start, currFreq = memo[num]
            if currFreq > maxFreq:
                maxFreq = currFreq
                minLen = end - start + 1
            elif currFreq == maxFreq:
                minLen = min(minLen, end - start + 1)

        return minLen


print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
