"""
https://leetcode.com/problems/sum-of-even-numbers-after-queries/
"""


class Solution:
    def sumEvenAfterQueries(
            self, nums: list[int], queries: list[list[int]]) -> list[int]:
        currSum = sum(num for num in nums if num & 1 == 0)
        rslt = []
        for val, i in queries:
            if nums[i] & 1 == 0:
                currSum -= nums[i]

            nums[i] += val
            if nums[i] & 1 == 0:
                currSum += nums[i]

            rslt.append(currSum)

        return rslt


print(Solution().sumEvenAfterQueries([1, 2, 3, 4],
                                     [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
