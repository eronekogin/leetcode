"""
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
"""


class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        start, currSum, minLen = 0, 0, float('inf')
        preMin = [float('inf')] * len(arr)
        for end, num in enumerate(arr):
            currSum += num
            while currSum > target:
                currSum -= arr[start]
                start += 1

            if currSum == target:
                currLen = end - start + 1
                minLen = min(minLen, currLen + preMin[start - 1])
                preMin[end] = min(currLen, preMin[end - 1])
            else:
                preMin[end] = preMin[end - 1]

        if minLen == float('inf'):
            return -1

        return minLen


print(Solution().minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1],
                                 3))
