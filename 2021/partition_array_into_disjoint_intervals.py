"""
https://leetcode.com/problems/partition-array-into-disjoint-intervals/
"""


class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        N = len(nums)
        maxLefts, minRights = [None] * N, [None] * N

        # Scan from left to right to get max lefts.
        currMax = nums[0]
        for i in range(N):
            if nums[i] > currMax:
                currMax = nums[i]

            maxLefts[i] = currMax

        # Scan from right to left to get min rights.
        currMin = nums[-1]
        for i in reversed(range(N)):
            if nums[i] < currMin:
                currMin = nums[i]

            minRights[i] = currMin

        # Then check the smallest cut position.
        for i in range(N - 1):
            if maxLefts[i] <= minRights[i + 1]:
                return i + 1


print(Solution().partitionDisjoint([5, 0, 3, 8, 6]))
