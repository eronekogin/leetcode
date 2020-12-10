"""
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
"""


from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        subSums = []  # Sum of subarrays with length k starting at index i.
        currSum = 0
        for i, num in enumerate(nums):  # Calculate subsums.
            currSum += num
            if i >= k:
                currSum -= nums[i - k]

            if i >= k - 1:
                subSums.append(currSum)

        n = len(subSums)
        lefts, currMax = [0] * n, 0
        for i in range(n):
            if subSums[i] > subSums[currMax]:  # Record the smallest index.
                currMax = i

            lefts[i] = currMax

        rights, currMax = [0] * n, n - 1
        for i in range(n - 1, -1, -1):
            if subSums[i] >= subSums[currMax]:  # Record the smallest index.
                currMax = i

            rights[i] = currMax

        leftMax = midMax = rightMax = None
        for m in range(k, n - k):
            l, r = lefts[m - k], rights[m + k]
            if leftMax is None or subSums[l] + subSums[m] + subSums[r] > \
                    subSums[leftMax] + subSums[midMax] + subSums[rightMax]:
                leftMax, midMax, rightMax = l, m, r

        return (leftMax, midMax, rightMax)
