"""
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
"""


class Solution:
    def maxSumTwoNoOverlap(
        self, nums: list[int], firstLen: int, secondLen: int
    ) -> int:
        def get_max_sum_of_subarray_with_length(start: int, end: int) -> int:
            if firstLen > end - 1 - start:
                return 0

            maxSum = float('-inf')
            for i in range(start + firstLen, end):
                maxSum = max(maxSum, preSums[i] - preSums[i - firstLen])

            return maxSum

        N = len(nums)
        preSums = [0]

        # Calculate pre summaries first.
        for num in nums:
            preSums.append(preSums[-1] + num)

        maxSum = float('-inf')
        for end in range(secondLen, N + 1):
            secondSum = preSums[end] - preSums[end - secondLen]
            firstSum = max(
                get_max_sum_of_subarray_with_length(0, end - secondLen + 1),
                get_max_sum_of_subarray_with_length(end, N + 1)
            )
            maxSum = max(maxSum, firstSum + secondSum)

        return maxSum


print(Solution().maxSumTwoNoOverlap(
    [8, 20, 6, 2, 20, 17, 6, 3, 20, 8, 12], 5, 4))
