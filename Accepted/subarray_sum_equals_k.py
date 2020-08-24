"""
https://leetcode.com/problems/subarray-sum-equals-k/
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rslt = 0
        sums = {0: 1}  # subsum: occurred times.
        currSum = 0  # The cumulative sum up to the ith number in nums.
        for num in nums:
            currSum += num
            rslt += sums.get(currSum - k, 0)
            sums[currSum] = sums.get(currSum, 0) + 1

        return rslt
