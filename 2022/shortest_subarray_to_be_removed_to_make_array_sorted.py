"""
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        N = len(arr)
        minEnd = N - 1

        while minEnd > 0 and arr[minEnd - 1] <= arr[minEnd]:
            minEnd -= 1

        if minEnd == 0:  # The whole array is already sorted.
            return 0

        maxStart = 0
        while maxStart < minEnd and arr[maxStart] <= arr[maxStart + 1]:
            maxStart += 1

        minRemoves = min(minEnd, N - maxStart - 1)
        start, end = 0, minEnd
        while start <= maxStart and end < N:
            if arr[start] <= arr[end]:
                minRemoves = min(minRemoves, end - start - 1)
                start += 1
            else:
                end += 1

        return minRemoves


print(Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
