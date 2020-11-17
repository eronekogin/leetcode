"""
https://leetcode.com/problems/find-k-closest-elements/
"""


from typing import List


from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if not n or k > n:
            return []

        if x < arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[n - k:]

        t = bisect_left(arr, x)
        left, right = max(0, t - k), min(t + (k - 1), n - 1)
        while right - left + 1 > k:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1

        return arr[left: right + 1]


print(Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))
