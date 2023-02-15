"""
https://leetcode.com/problems/closest-subsequence-sum/
"""


from bisect import bisect_left


class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        def gen_subseq_sum(
            i: int,
            currSum: int,
            nums: list[int],
            sums: set[int]
        ):
            if i == len(nums):
                sums.add(currSum)
                return

            gen_subseq_sum(i + 1, currSum, nums, sums)
            gen_subseq_sum(i + 1, currSum + nums[i], nums, sums)

        leftSums, rightSums = set(), set()
        m = len(nums) >> 1
        gen_subseq_sum(0, 0, nums[:m], leftSums)
        gen_subseq_sum(0, 0, nums[m:], rightSums)

        rightSums = sorted(rightSums)

        rslt = float('inf')
        for leftSum in leftSums:
            rightSum = goal - leftSum
            r = bisect_left(rightSums, rightSum)
            if r < len(rightSums):
                rslt = min(rslt, abs(rightSum - rightSums[r]))

            if r > 0:
                rslt = min(rslt, abs(rightSum - rightSums[r - 1]))

        return rslt
