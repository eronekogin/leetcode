"""
https://leetcode.com/problems/k-concatenation-maximum-sum/
"""


class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        def max_subarray_sum(arr: list[int]) -> int:
            currSum = maxSum = 0
            for num in arr:
                currSum = max(num, currSum + num)
                maxSum = max(maxSum, currSum)

            return maxSum

        if k == 1:
            result = max_subarray_sum(arr)
        else:
            result = max_subarray_sum(arr + arr) + (k - 2) * max(sum(arr), 0)

        return result % (10 ** 9 + 7)
