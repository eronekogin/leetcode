"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        currSum = 0
        maxSum = k * threshold
        candidateCnt = 0
        for end, num in enumerate(arr):
            if end >= k:
                if currSum >= maxSum:
                    candidateCnt += 1

                currSum -= arr[end - k]

            currSum += num

        return candidateCnt + (currSum >= maxSum)  # Check the last item.


print(Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
