"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""


class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        """
        Consider a subarray that includes arr[i]:
            1. From left we could pick 0 elements to i elements, which provides
                us i + 1 solutions.
            2. From right we could pick 0 elements to n - 1 - i elements, which
                provides us n - i solutions.

        So the total number of subarrays that includes arr[i] is
            k = (i + 1) * (n - i)

        Then arrays with odd length is (k + 1) // 2
        """
        N = len(arr)
        return sum(
            ((i + 1) * (N - i) + 1) // 2 * num
            for i, num in enumerate(arr)
        )
