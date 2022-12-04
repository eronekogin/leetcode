"""
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
"""


class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        def calculate_result(i: int):
            # (p[N] - p[i + 1]) - (N - i - 1) * nums[i] + i * nums[i] - (P[i] - P[0])
            return (
                (prefixSums[N] - prefixSums[i + 1]) -
                (prefixSums[i] - prefixSums[0]) -
                (N - (i << 1) - 1) * nums[i]
            )

        N = len(nums)
        prefixSums: list[int] = [0]
        for num in nums:
            prefixSums.append(prefixSums[-1] + num)

        return [
            calculate_result(i)
            for i in range(N)
        ]


print(Solution().getSumAbsoluteDifferences([2, 3, 5]))
