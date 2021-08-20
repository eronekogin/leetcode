"""
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
"""


class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        remainChanges = k
        sortedNums = sorted(nums, key=lambda x: abs(x))
        for i in range(len(sortedNums) - 1, -1, -1):
            if sortedNums[i] < 0:
                remainChanges -= 1
                sortedNums[i] *= -1

            if not remainChanges:
                break

        if remainChanges:
            sortedNums[0] *= (-1) ** remainChanges

        return sum(sortedNums)


print(Solution().largestSumAfterKNegations(
    [-8, 3, -5, -3, -5, -2],
    6
))
